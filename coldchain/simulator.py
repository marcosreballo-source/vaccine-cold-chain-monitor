"""Simulador de leituras de temperatura de geladeiras de vacinas.

Gera séries realistas para várias UBS: ciclo do compressor em torno de 5 °C,
ruído do sensor (DS18B20, ±0,5 °C), e eventos que causam perdas na rede de frio
— queda de energia, porta aberta, falha de compressor e sensor offline.
Determinístico por `seed`, para demos e testes reprodutíveis.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

UBS_NAMES = [
    "UBS Vila Isabel", "UBS Santa Felícia", "UBS Cidade Aracy", "UBS Redenção",
    "UBS Jardim São Rafael", "UBS Santa Paula", "UBS Vila São José", "UBS Azulville",
    "UBS Botafogo", "UBS Santa Eudóxia", "UBS Água Vermelha",
]  # bairros de São Carlos; unidades e dados são fictícios

INVENTORY_SEED = 7  # rede fixa de UBS/câmaras, independente do cenário simulado


@dataclass(frozen=True)
class Event:
    fridge_id: str
    kind: str          # power_outage | door_open | compressor_failure | sensor_offline
    start: pd.Timestamp
    minutes: int


def build_fridges(n_ubs: int = 11, seed: int = 7) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for i, name in enumerate(UBS_NAMES[:n_ubs]):
        for j in range(1 + int(rng.random() < 0.4)):  # algumas UBS têm 2 câmaras
            rows.append({
                "fridge_id": f"U{i + 1:02d}-G{j + 1}",
                "ubs": name,
                "model": rng.choice(["Câmara científica 280L", "Câmara científica 120L", "Refrigerador doméstico"]),
                "setpoint": round(float(rng.uniform(4.5, 5.5)), 1),
                "doses_stored": int(rng.integers(300, 2500)),
            })
    return pd.DataFrame(rows)


def schedule_events(fridges: pd.DataFrame, start: pd.Timestamp, days: int, seed: int = 7) -> list[Event]:
    rng = np.random.default_rng(seed + 1)
    events: list[Event] = []
    total_min = days * 24 * 60
    for fid, model in zip(fridges.fridge_id, fridges.model):
        # Refrigerador doméstico (não recomendado pelo PNI) falha mais
        fragility = 2.0 if model == "Refrigerador doméstico" else 1.0
        for kind, rate_per_week, dur in [
            ("door_open", 2.0, (2, 14)),
            ("power_outage", 0.4, (40, 240)),
            ("compressor_failure", 0.15, (180, 600)),
            ("sensor_offline", 0.3, (20, 180)),
        ]:
            n = rng.poisson(rate_per_week * fragility * days / 7)
            for _ in range(n):
                offset = int(rng.integers(0, max(1, total_min - dur[1])))
                events.append(Event(fid, kind, start + pd.Timedelta(minutes=offset),
                                    int(rng.integers(*dur))))
    return sorted(events, key=lambda e: e.start)


def live_events(fridges: pd.DataFrame, end: pd.Timestamp, seed: int = 7) -> list[Event]:
    """Eventos em andamento no 'agora', para a demo mostrar os estados ALARME, ATENÇÃO e OFFLINE."""
    rng = np.random.default_rng(seed + 3)
    picks = rng.choice(fridges.fridge_id.to_numpy(), size=min(3, len(fridges)), replace=False)
    specs = [("power_outage", 75), ("compressor_failure", 110), ("sensor_offline", 35)]
    return [Event(fid, kind, end - pd.Timedelta(minutes=mins), mins + 1) for fid, (kind, mins) in zip(picks, specs)]


def simulate(days: int = 7, freq_s: int = 60, n_ubs: int = 11, seed: int = 7,
             end: pd.Timestamp | None = None, live: bool = True) -> tuple[pd.DataFrame, pd.DataFrame, list[Event]]:
    """Retorna (leituras, geladeiras, eventos). Leituras: timestamp, fridge_id, temp_c (NaN = sem sinal)."""
    end = (end or pd.Timestamp.now(tz="America/Sao_Paulo")).floor("min")
    start = end - pd.Timedelta(days=days)
    idx = pd.date_range(start, end, freq=f"{freq_s}s", inclusive="left")
    # O inventário (UBS e câmaras) é fixo: o `seed` muda só o cenário de eventos.
    fridges = build_fridges(n_ubs, INVENTORY_SEED)
    events = schedule_events(fridges, start, days, seed)
    if live:
        events = sorted(events + live_events(fridges, end, seed), key=lambda e: e.start)
    rng = np.random.default_rng(seed + 2)
    t_min = (idx - start).total_seconds().to_numpy() / 60

    frames = []
    for f in fridges.itertuples():
        period = rng.uniform(25, 45)                       # ciclo do compressor (min)
        temp = f.setpoint + 0.8 * np.sin(2 * np.pi * t_min / period + rng.uniform(0, 6.28))
        temp += rng.normal(0, 0.15, len(idx))              # ruído do sensor
        # sala mais quente à tarde puxa a câmara levemente para cima
        hours = idx.hour.to_numpy() + idx.minute.to_numpy() / 60
        temp += 0.3 * np.clip(np.sin((hours - 9) / 24 * 2 * np.pi), 0, None)

        for ev in (e for e in events if e.fridge_id == f.fridge_id):
            s = int((ev.start - start).total_seconds() // freq_s)
            n = max(1, ev.minutes * 60 // freq_s)
            seg = slice(s, min(s + n, len(idx)))
            k = np.arange(seg.stop - seg.start) * freq_s / 60
            if ev.kind == "door_open":
                temp[seg] += np.minimum(0.3 * k, 3.5)
            elif ev.kind == "power_outage":
                temp[seg] += 9.0 * (1 - np.exp(-k / 70))  # aquece rumo à temperatura ambiente
            elif ev.kind == "compressor_failure":
                temp[seg] += 0.02 * k                     # deriva lenta: o caso que o alerta antecipado pega
            # recuperação depois do evento (o compressor puxa de volta)
            if ev.kind in ("door_open", "power_outage", "compressor_failure") and seg.stop < len(idx):
                excess = temp[seg.stop - 1] - f.setpoint
                rec = slice(seg.stop, min(seg.stop + 90 * 60 // freq_s, len(idx)))
                kk = np.arange(rec.stop - rec.start) * freq_s / 60
                temp[rec] += excess * np.exp(-kk / 12)
        temp = np.round(temp, 2)
        for ev in (e for e in events if e.fridge_id == f.fridge_id and e.kind == "sensor_offline"):
            s = int((ev.start - start).total_seconds() // freq_s)
            temp[s:s + ev.minutes * 60 // freq_s] = np.nan
        frames.append(pd.DataFrame({"timestamp": idx, "fridge_id": f.fridge_id, "temp_c": temp}))

    readings = pd.concat(frames, ignore_index=True)
    return readings, fridges, events
