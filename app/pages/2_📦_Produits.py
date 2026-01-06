import streamlit as st
import plotly.express as px

#avant de lire la DB avec read sql, il faut en forcer la création
from app.utils.db import ensure_db
ensure_db()

from app.utils.db import read_sql
from app.utils.queries import (
    Q_MINMAX_YEAR, Q_DIM_GENRES, Q_DIM_PLATFORMS, Q_DIM_PUBLISHERS,
    REGIONS, build_where_clause, q_top_games, q_top_dim
)


st.set_page_config(page_title="Top", layout="wide")
st.title("🏆 Tops – Jeux / Plateformes / Éditeurs")

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

top_n = st.sidebar.slider("Top N", 5, 30, 15)

where, params = build_where_clause(ymin, ymax, genre, platform, publisher)

colA, colB = st.columns(2)

with colA:
    top_games = read_sql(q_top_games(where, sales_col, limit=top_n), params=params)
    fig1 = px.bar(top_games, x="sales", y="game_name", orientation="h", title=f"Top {top_n} jeux – {region}")
    st.plotly_chart(fig1, use_container_width=True)

with colB:
    top_pub = read_sql(q_top_dim(where, sales_col, dim="publisher", limit=top_n), params=params)
    fig2 = px.bar(top_pub, x="sales", y="label", orientation="h", title=f"Top {top_n} éditeurs – {region}")
    st.plotly_chart(fig2, use_container_width=True)

top_plat = read_sql(q_top_dim(where, sales_col, dim="platform", limit=top_n), params=params)
fig3 = px.bar(top_plat, x="sales", y="label", orientation="h", title=f"Top {top_n} plateformes – {region}")
st.plotly_chart(fig3, use_container_width=True)


