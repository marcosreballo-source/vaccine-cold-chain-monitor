"""Testes da interface com o AppTest do Streamlit (roda o app sem navegador)."""

import re
from pathlib import Path

from streamlit.testing.v1 import AppTest

from coldchain.simulator import UBS_NAMES

APP = str(Path(__file__).resolve().parents[1] / "app.py")


def _cards(at) -> list[str]:
    html = "".join(m.value for m in at.markdown)
    return re.findall(r"<b>(UBS [^<]+)</b>", html)


def _run(**changes):
    at = AppTest.from_file(APP, default_timeout=60).run()
    for label, value in changes.items():
        widget = next(w for w in [*at.slider, *at.number_input] if w.label.startswith(label))
        widget.set_value(value)
    return at.run()


def test_one_card_per_ubs_and_same_network_across_scenarios():
    for seed in (7, 8, 9):
        at = _run(**{"Cenário simulado": seed})
        assert not at.exception
        cards = _cards(at)
        assert sorted(cards) == sorted(UBS_NAMES)  # 11 UBS, nenhuma repetida


def test_controls_change_what_is_shown():
    base = _run()
    longer = _run(**{"Período analisado (dias)": 14})
    strict = _run(**{"Excursão vira incidente após (min)": 1})
    metric = lambda at, prefix: next(m.value for m in at.metric if m.label.startswith(prefix))
    assert metric(base, "Incidentes em 7 d") != metric(strict, "Incidentes em 7 d")
    assert "14 d:" in "".join(m.value for m in longer.markdown)
    assert any(m.label.startswith("Incidentes em 14 d") for m in longer.metric)
