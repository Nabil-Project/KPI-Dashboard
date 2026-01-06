from pathlib import Path
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# ---- BOOTSTRAP DB (création si absente)
def ensure_db():
    base_dir = Path(__file__).resolve().parents[2]
    raw_csv = base_dir / "data" / "raw" / "vgsales.csv"
    db_path = base_dir / "data" / "processed" / "ecommerce.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)

    if db_path.exists():
        return

    df = pd.read_csv(raw_csv)

    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df = df.dropna(subset=["Year"])
    df["Year"] = df["Year"].astype(int)

    for col in ["Name", "Platform", "Genre", "Publisher"]:
        df[col] = df[col].fillna("Unknown")

    sales_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
    for c in sales_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0)

    df = df.rename(columns={
        "Name": "game_name",
        "Platform": "platform",
        "Genre": "genre",
        "Publisher": "publisher",
        "Global_Sales": "global_sales",
        "NA_Sales": "na_sales",
        "EU_Sales": "eu_sales",
        "JP_Sales": "jp_sales",
        "Other_Sales": "other_sales"
    })

    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql("vgsales", engine, if_exists="replace", index=False)


@st.cache_resource
def get_engine():
    ensure_db()  # 🔥 LA LIGNE CRITIQUE
    base_dir = Path(__file__).resolve().parents[2]
    db_path = base_dir / "data" / "processed" / "ecommerce.db"
    return create_engine(f"sqlite:///{db_path}")


@st.cache_data
def read_sql(query: str, params=None) -> pd.DataFrame:
    engine = get_engine()
    return pd.read_sql(query, engine, params=params)
