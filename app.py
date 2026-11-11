"""Painel de monitoramento da rede de frio de vacinas — UBS de São Carlos (dados simulados).

Rodar: streamlit run app.py
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from coldchain.analytics import Thresholds, doses_at_risk, fridge_status, incidents
from coldchain.simulator import simulate

st.set_page_config(page_title="Rede de Frio · UBS São Carlos", page_icon="🧊", layout="wide")

STATUS_COLOR = {"ALARME": "#d64545", "OFFLINE": "#7a7a7a", "ATENÇÃO": "#e0a800", "OK": "#2e9e5b"}
CAUSE = {"door_open": "porta aberta", "power_outage": "queda de energia",
         "compressor_failure": "falha de compressor", "sensor_offline": "sensor sem sinal"}


@st.cache_data(ttl=600)
def load(days: int, seed: int):
    readings, fridges, events = simulate(days=days, seed=seed)
    ev = pd.DataFrame([e.__dict__ for e in events])
    return readings, fridges, ev


with st.sidebar:
    st.header("Configuração")
    days = st.slider("Histórico (dias)", 1, 14, 7)
    seed = st.number_input("Cenário (seed)", 1, 999, 7, help="Muda o cenário simulado")
    st.divider()
    th = Thresholds(
        incident_min_minutes=st.slider("Excursão vira incidente após (min)", 1, 60, 10),
        forecast_horizon_minutes=st.slider("Alerta antecipado: horizonte (min)", 15, 180, 60),
    )
    st.caption("Faixa de conservação: +2 °C a +8 °C (Manual de Rede de Frio / PNI).")
    st.caption("Dados **simulados** para demonstração; UBS e leituras são fictícias.")

readings, fridges, events = load(days, int(seed))
now = readings.timestamp.max()
status = fridge_status(readings, fridges, now, th)
inc = incidents(readings, th).merge(fridges[["fridge_id", "ubs"]], on="fridge_id")

st.title("🧊 Rede de Frio — UBS São Carlos")
st.caption(f"Última leitura: {now:%d/%m/%Y %H:%M} · {len(fridges)} câmaras em {fridges.ubs.nunique()} UBS · leitura a cada 1 min")

c = st.columns(5)
counts = status.status.value_counts()
c[0].metric("Em alarme", int(counts.get("ALARME", 0)))
c[1].metric("Atenção (tendência)", int(counts.get("ATENÇÃO", 0)))
c[2].metric("Offline", int(counts.get("OFFLINE", 0)))
c[3].metric("Incidentes no período", int(inc.is_incident.sum()))
c[4].metric("Doses a avaliar", f"{doses_at_risk(status, inc, now):,}".replace(",", "."))

tab_overview, tab_detail, tab_incidents = st.tabs(["Visão geral", "Câmara", "Incidentes"])

with tab_overview:
    cols = st.columns(4)
    for i, row in enumerate(status.itertuples()):
        with cols[i % 4]:
            color = STATUS_COLOR[row.status]
            eta = f"<br>⏱ sai da faixa em ~{row.min_para_sair_da_faixa:.0f} min" if row.min_para_sair_da_faixa is not None and row.status == "ATENÇÃO" else ""
            temp = "—" if pd.isna(row.temp_atual) or row.status == "OFFLINE" else f"{row.temp_atual:.1f} °C"
            st.markdown(
                f"""<div style="border-left:6px solid {color};padding:8px 12px;margin-bottom:10px;
                border-radius:6px;background:rgba(127,127,127,0.08)">
                <b>{row.ubs}</b> <span style="opacity:.7">({row.fridge_id})</span><br>
                <span style="font-size:1.6em">{temp}</span>
                <span style="color:{color};font-weight:600;float:right">{row.status}</span><br>
                <span style="opacity:.75">24h: {row.min_24h:.1f}–{row.max_24h:.1f} °C ·
                em faixa {row.tempo_em_faixa_24h_pct:.0f}%</span>{eta}</div>""",
                unsafe_allow_html=True,
            )
    st.subheader("Tempo em faixa nas últimas 24 h")
    st.bar_chart(status.set_index("fridge_id")["tempo_em_faixa_24h_pct"], height=220)

with tab_detail:
    # ordem por gravidade: abre direto na câmara mais crítica
    options = [f"{r.fridge_id} · {r.ubs} · {r.status}" for r in status.itertuples()]
    choice = st.selectbox("Câmara", options)
    fid = choice.split(" · ")[0]
    g = readings[readings.fridge_id == fid]
    fig = go.Figure()
    fig.add_hrect(y0=th.low, y1=th.high, fillcolor="green", opacity=0.08, line_width=0)
    fig.add_hline(y=th.high, line_dash="dash", line_color="#d64545")
    fig.add_hline(y=th.low, line_dash="dash", line_color="#3b6fd6")
    fig.add_trace(go.Scatter(x=g.timestamp, y=g.temp_c, mode="lines", name="Temperatura", line=dict(width=1.2)))
    for e in events[events.fridge_id == fid].itertuples():
        x1 = e.start + pd.Timedelta(minutes=e.minutes)
        if e.kind == "door_open":  # frequente: só sombreia, sem rótulo
            fig.add_vrect(x0=e.start, x1=x1, fillcolor="gray", opacity=0.08, line_width=0)
        else:
            fig.add_vrect(x0=e.start, x1=x1, fillcolor="orange", opacity=0.15, line_width=0,
                          annotation_text=CAUSE[e.kind], annotation_position="top left", annotation_font_size=10)
    fig.update_xaxes(
        range=[now - pd.Timedelta(hours=24), now],
        rangeselector=dict(buttons=[dict(count=6, label="6h", step="hour", stepmode="backward"),
                                    dict(count=24, label="24h", step="hour", stepmode="backward"),
                                    dict(count=7, label="7d", step="day", stepmode="backward"),
                                    dict(step="all", label="tudo")]),
    )
    fig.update_layout(height=420, yaxis_title="°C", margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)
    st.caption("Faixas laranja: eventos simulados (a causa real seria registrada pela equipe da UBS).")
    st.dataframe(inc[inc.fridge_id == fid].drop(columns=["fridge_id"]), hide_index=True, use_container_width=True)

with tab_incidents:
    only = st.toggle("Só incidentes (acima da tolerância)", value=True)
    view = inc[inc.is_incident] if only else inc
    st.dataframe(
        view[["ubs", "fridge_id", "start", "end", "minutes", "peak_c", "direction"]]
        .rename(columns={"ubs": "UBS", "fridge_id": "Câmara", "start": "Início", "end": "Fim",
                         "minutes": "Duração (min)", "peak_c": "Pico (°C)", "direction": "Excursão"}),
        hide_index=True, use_container_width=True,
    )
    by_ubs = view.groupby("ubs").minutes.agg(["count", "sum"]).rename(columns={"count": "incidentes", "sum": "minutos fora"})
    st.subheader("Por UBS")
    st.dataframe(by_ubs.sort_values("minutos fora", ascending=False), use_container_width=True)
    st.download_button("Baixar CSV (relatório de conformidade)", view.to_csv(index=False).encode("utf-8"),
                       "incidentes_rede_de_frio.csv", "text/csv")
