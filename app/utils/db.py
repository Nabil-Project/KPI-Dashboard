from pathlib import Path
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

@st.cache_resource
def get_engine():
    base_dir = Path(__file__).resolve().parents[2]  # -> data_dashboard/
    db_path = base_dir / "data" / "processed" / "ecommerce.db"
    return create_engine(f"sqlite:///{db_path}")

@st.cache_data
def read_sql(query: str, params=None) -> pd.DataFrame:
    engine = get_engine()
    return pd.read_sql(query, engine, params=params)
