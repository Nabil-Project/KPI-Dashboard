import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
DB_PATH = BASE_DIR / "data" / "processed" / "ecommerce.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(f"sqlite:///{DB_PATH}")

# ---- Load
df = pd.read_csv(RAW_DIR / "vgsales.csv")

# ---- Clean
# Year peut être vide => on force en numérique
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df = df.dropna(subset=["Year"])
df["Year"] = df["Year"].astype(int)

# Remplacer les NA Publisher/Genre/Platform/Name
for col in ["Name", "Platform", "Genre", "Publisher"]:
    df[col] = df[col].fillna("Unknown")

# Sales en numérique
sales_cols = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
for c in sales_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0)

# ---- Rename columns (optionnel mais plus clean)
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

#Débug permettant de savoir si le graph remonte bien aavnt 2000 car on a des données allant jusqu'à 1980
print("DEBUG rows:", len(df))
print("DEBUG min year:", df["Year"].min(), "DEBUG max year:", df["Year"].max())
print("DEBUG years sample:", sorted(df["Year"].unique())[:10])


df.to_sql("vgsales", engine, if_exists="replace", index=False)

print("✅ vgsales.csv loaded into SQLite table: vgsales")
