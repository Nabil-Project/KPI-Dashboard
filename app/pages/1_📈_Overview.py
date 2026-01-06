import streamlit as st
import plotly.express as px

from utils.db import read_sql
from utils.queries import (
    Q_MINMAX_YEAR, Q_DIM_GENRES, Q_DIM_PLATFORMS, Q_DIM_PUBLISHERS,
    REGIONS, build_where_clause, q_kpi, q_sales_by_year
)


st.set_page_config(page_title="Overview", layout="wide")
st.title("🎮 Video Game Sales – Overview")

# ---- Sidebar filters (style vidéo)
st.sidebar.header("Filtres")

minmax = read_sql(Q_MINMAX_YEAR).iloc[0]
min_y, max_y = int(minmax["min_y"]), int(minmax["max_y"])

ymin, ymax = st.sidebar.slider("Années", min_y, max_y, (min_y, max_y))

region = st.sidebar.selectbox("Région (ventes)", list(REGIONS.keys()))
sales_col = REGIONS[region]

genres = ["All"] + read_sql(Q_DIM_GENRES)["genre"].tolist()
platforms = ["All"] + read_sql(Q_DIM_PLATFORMS)["platform"].tolist()
publishers = ["All"] + read_sql(Q_DIM_PUBLISHERS)["publisher"].tolist()

genre = st.sidebar.selectbox("Genre", genres)
platform = st.sidebar.selectbox("Plateforme", platforms)
publisher = st.sidebar.selectbox("Éditeur", publishers)

st.sidebar.caption("Astuce : clique sur une liste et commence à taper pour rechercher (plateforme / éditeur).")


#clé de lecture

st.sidebar.markdown("### 🔎 Résumé filtres")
st.sidebar.write(f"Années : {ymin} → {ymax}")
st.sidebar.write(f"Région : {region}")
st.sidebar.write(f"Genre : {genre}")
st.sidebar.write(f"Plateforme : {platform}")
st.sidebar.write(f"Éditeur : {publisher}")



where, params = build_where_clause(ymin, ymax, genre, platform, publisher)

# ---- KPIs
kpi = read_sql(q_kpi(where, sales_col), params=params).iloc[0]


c1, c2, c3, c4 = st.columns(4)

sales_m = float(kpi["sales"] or 0)  # ventes en millions d'unités
c1.metric("Ventes (unités)", f"{sales_m:,.2f} M")

c2.metric("Entrées (lignes)", int(kpi["nb_rows"] or 0))
c3.metric("Jeux uniques", int(kpi["nb_games"] or 0))
c4.metric("Éditeurs uniques", int(kpi["nb_publishers"] or 0))

#clé de lecture pourcomprendre comment lire les données
st.caption("ℹ️ Les colonnes de ventes (NA/EU/JP/Global) sont exprimées en **millions d’unités vendues** dans ce dataset.")


# ---- Trend
ts = read_sql(q_sales_by_year(where, sales_col), params=params)
fig = px.line(ts, x="Year", y="sales", title=f"Ventes par année – {region}")
st.plotly_chart(fig, use_container_width=True)
