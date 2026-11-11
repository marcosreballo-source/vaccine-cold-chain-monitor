import numpy as np
import pandas as pd
import pytest

from coldchain.analytics import Thresholds, doses_at_risk, fridge_status, incidents, minutes_to_exit
from coldchain.simulator import simulate

NOW = pd.Timestamp("2026-11-10 12:00", tz="America/Sao_Paulo")


def _series(values, fid="F1", step_min=1, end=NOW):
    idx = pd.date_range(end=end - pd.Timedelta(minutes=step_min), periods=len(values), freq=f"{step_min}min")
    return pd.DataFrame({"timestamp": idx, "fridge_id": fid, "temp_c": values})


def _fridges(*ids):
    return pd.DataFrame({"fridge_id": ids, "ubs": [f"UBS {i}" for i in ids], "model": "x",
                         "doses_stored": [100] * len(ids)})


def test_incident_detection_duration_and_tolerance():
    vals = [5.0] * 10 + [9.0] * 15 + [5.0] * 10 + [1.5] * 3 + [5.0] * 5
    inc = incidents(_series(vals))
    assert len(inc) == 2
    hot = inc[inc.direction.str.startswith("acima")].iloc[0]
    cold = inc[inc.direction.str.startswith("abaixo")].iloc[0]
    assert hot.minutes == 15 and hot.is_incident and hot.peak_c == 9.0
    assert cold.minutes == 3 and not cold.is_incident  # curta demais para incidente


def test_minutes_to_exit_projects_rising_trend():
    times = pd.Series(pd.date_range(NOW - pd.Timedelta(minutes=89), NOW, freq="1min"))
    rising = pd.Series(np.linspace(5.0, 7.0, 90))  # ~0,022 °C/min a partir de 7 °C → sai em ~44 min
    eta = minutes_to_exit(rising, times)
    assert eta is not None and 35 < eta < 55
    flat = pd.Series(np.full(90, 5.0))
    assert minutes_to_exit(flat, times) is None
    # oscilação normal do compressor (±0,8 °C, ciclo de 35 min) não pode gerar alerta
    t = np.arange(90)
    cycling = pd.Series(5.5 + 0.8 * np.sin(2 * np.pi * t / 35))
    assert minutes_to_exit(cycling, times) is None


def test_status_classification():
    readings = pd.concat([
        _series([5.0] * 60, "OK1"),
        _series([5.0] * 50 + [9.5] * 10, "ALM"),
        _series(list(np.linspace(5.0, 7.5, 60)), "ATN"),
        _series([5.0] * 30, "OFF", end=NOW - pd.Timedelta(minutes=40)),
    ])
    st = fridge_status(readings, _fridges("OK1", "ALM", "ATN", "OFF"), NOW, Thresholds())
    got = dict(zip(st.fridge_id, st.status))
    assert got == {"OK1": "OK", "ALM": "ALARME", "ATN": "ATENÇÃO", "OFF": "OFFLINE"}
    assert list(st.status)[:2] == ["ALARME", "OFFLINE"]  # pior primeiro


def test_doses_at_risk_counts_alarm_and_recent_incidents():
    readings = pd.concat([_series([5.0] * 50 + [9.5] * 10, "ALM"), _series([5.0] * 60, "OK1")])
    fr = _fridges("ALM", "OK1")
    st = fridge_status(readings, fr, NOW)
    assert doses_at_risk(st, incidents(readings), NOW) == 100


def test_simulator_is_deterministic_and_realistic():
    end = pd.Timestamp("2026-11-10 12:00", tz="America/Sao_Paulo")
    r1, fr, ev = simulate(days=2, seed=3, end=end)
    r2, _, _ = simulate(days=2, seed=3, end=end)
    pd.testing.assert_frame_equal(r1, r2)
    assert fr.ubs.nunique() == 11
    assert set(r1.fridge_id) == set(fr.fridge_id)
    in_range = r1.temp_c.between(2, 8).mean()
    assert 0.85 < in_range < 1.0  # quase sempre em faixa, com excursões ocasionais
    assert {e.kind for e in ev} >= {"door_open"}
