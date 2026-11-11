"""Regras de negócio da rede de frio.

Faixa de conservação de vacinas (PNI / Manual de Rede de Frio): +2 °C a +8 °C.
- Excursão: período contínuo fora da faixa. Excursões curtas (< tolerância)
  são registradas mas não viram incidente (ex.: porta aberta por segundos).
- Alerta antecipado: a tendência recente projeta saída da faixa em até N minutos,
  dando tempo de agir antes da perda — o ganho principal sobre a leitura manual 3x/dia.
- Offline: sem leitura há mais de N minutos (sensor, Wi-Fi ou energia do ESP32).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

LOW, HIGH = 2.0, 8.0


@dataclass(frozen=True)
class Thresholds:
    low: float = LOW
    high: float = HIGH
    incident_min_minutes: int = 10      # excursões menores que isso não abrem incidente
    offline_after_minutes: int = 10
    forecast_window_minutes: int = 90   # janela usada para estimar a tendência
    smoothing_minutes: int = 40         # ~1 ciclo do compressor: evita alarme falso pela oscilação normal
    forecast_horizon_minutes: int = 60  # avisa se a projeção sai da faixa dentro deste horizonte


def incidents(readings: pd.DataFrame, th: Thresholds = Thresholds()) -> pd.DataFrame:
    """Uma linha por excursão contínua fora da faixa, com duração e pico."""
    cols = ["fridge_id", "start", "end", "minutes", "peak_c", "direction", "is_incident"]
    out = []
    for fid, g in readings.dropna(subset=["temp_c"]).groupby("fridge_id", sort=False):
        g = g.sort_values("timestamp")
        out_mask = (g.temp_c < th.low) | (g.temp_c > th.high)
        if not out_mask.any():
            continue
        run_id = (out_mask != out_mask.shift()).cumsum()
        step = g.timestamp.diff().median() if len(g) > 1 else pd.Timedelta(minutes=1)
        for _, run in g[out_mask].groupby(run_id[out_mask]):
            start, end = run.timestamp.iloc[0], run.timestamp.iloc[-1] + step
            minutes = (end - start).total_seconds() / 60
            hot = run.temp_c.max() > th.high
            out.append({
                "fridge_id": fid, "start": start, "end": end, "minutes": round(minutes, 1),
                "peak_c": run.temp_c.max() if hot else run.temp_c.min(),
                "direction": "acima de 8 °C" if hot else "abaixo de 2 °C",
                "is_incident": minutes >= th.incident_min_minutes,
            })
    return pd.DataFrame(out, columns=cols).sort_values("start", ascending=False, ignore_index=True)


def minutes_to_exit(series: pd.Series, times: pd.Series, th: Thresholds = Thresholds()) -> float | None:
    """Projeção linear da tendência recente: em quantos minutos sai da faixa (None se não sai no horizonte)."""
    if len(series) < 5:
        return None
    series = series.reset_index(drop=True)
    times = times.reset_index(drop=True)
    step = max(times.diff().median().total_seconds() / 60, 1e-6)
    window = max(1, int(th.smoothing_minutes / step))
    if len(series) >= window + 5:
        smooth = series.rolling(window).mean()  # só janelas completas
        keep = smooth.notna().to_numpy()
        values, ts = smooth[keep].to_numpy(), times[keep]
        lag = (window - 1) * step / 2  # a média móvel atrasa ~meia janela
    else:
        values, ts, lag = series.to_numpy(), times, 0.0
    t = (ts - times.iloc[-1]).dt.total_seconds().to_numpy() / 60
    slope, intercept = np.polyfit(t, values, 1)
    current = intercept + slope * lag
    if current < th.low or current > th.high:
        return 0.0
    if abs(slope) < 1e-3:
        return None
    limit = th.high if slope > 0 else th.low
    eta = (limit - current) / slope
    return float(eta) if 0 <= eta <= th.forecast_horizon_minutes else None


def fridge_status(readings: pd.DataFrame, fridges: pd.DataFrame, now: pd.Timestamp,
                  th: Thresholds = Thresholds(), window_hours: float = 24) -> pd.DataFrame:
    """Estado atual de cada geladeira: OK, ATENÇÃO (tendência de saída), ALARME (fora da faixa) ou OFFLINE.

    Mínimo, máximo, tempo em faixa e minutos fora são calculados sobre as últimas `window_hours`.
    """
    rows = []
    period = readings[readings.timestamp > now - pd.Timedelta(hours=window_hours)]
    for f in fridges.itertuples():
        g = period[period.fridge_id == f.fridge_id].sort_values("timestamp")
        valid = g.dropna(subset=["temp_c"])
        last_seen = valid.timestamp.max() if len(valid) else pd.NaT
        current = valid.temp_c.iloc[-1] if len(valid) else np.nan
        offline = pd.isna(last_seen) or (now - last_seen) > pd.Timedelta(minutes=th.offline_after_minutes)

        win = valid[valid.timestamp > (last_seen - pd.Timedelta(minutes=th.forecast_window_minutes))] if len(valid) else valid
        eta = None if offline else minutes_to_exit(win.temp_c, win.timestamp, th)

        in_range = valid.temp_c.between(th.low, th.high)
        tir = 100 * in_range.mean() if len(valid) else np.nan
        step_min = (valid.timestamp.diff().median().total_seconds() / 60) if len(valid) > 1 else 1
        if offline:
            status = "OFFLINE"
        elif not (th.low <= current <= th.high):
            status = "ALARME"
        elif eta is not None:
            status = "ATENÇÃO"
        else:
            status = "OK"
        rows.append({
            "fridge_id": f.fridge_id, "ubs": f.ubs, "model": f.model, "doses_stored": f.doses_stored,
            "status": status, "temp_atual": current, "min_periodo": valid.temp_c.min(), "max_periodo": valid.temp_c.max(),
            "tempo_em_faixa_pct": tir, "min_fora": float((~in_range).sum() * step_min),
            "min_para_sair_da_faixa": eta, "ultima_leitura": last_seen,
        })
    order = {"ALARME": 0, "OFFLINE": 1, "ATENÇÃO": 2, "OK": 3}
    df = pd.DataFrame(rows)
    return df.sort_values(by="status", key=lambda s: s.map(order), kind="stable", ignore_index=True)


def doses_at_risk(status: pd.DataFrame, incident_table: pd.DataFrame, now: pd.Timestamp) -> int:
    """Doses em geladeiras com alarme agora ou com incidente nas últimas 24 h (precisam de avaliação técnica)."""
    flagged: set[str] = set()
    if not incident_table.empty:
        recent = incident_table[incident_table.is_incident & (incident_table.end > now - pd.Timedelta(hours=24))]
        flagged = set(recent.fridge_id)
    flagged |= set(status.loc[status.status == "ALARME", "fridge_id"])
    return int(status.loc[status.fridge_id.isin(flagged), "doses_stored"].sum())
