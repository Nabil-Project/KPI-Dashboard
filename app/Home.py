import streamlit as st

st.set_page_config(page_title="Video Game Sales Dashboard", layout="wide")

st.title("🎮 Video Game Sales Dashboard")
st.write(
    """
Dashboard interactif **Data Analyst** (Python + SQL + Streamlit) pour explorer les ventes de jeux vidéo
par **année**, **genre**, **plateforme**, **éditeur** et **région**.

➡️ Utilise le menu à gauche pour ouvrir :
- **Overview**
- **Produits**
"""
)

st.markdown("### ✅ Ce que montre ce projet")
st.markdown(
    """
- Chargement + nettoyage de données (pandas)  
- Modélisation en base **SQLite**  
- Requêtes **SQL** (agrégations, tops, tendances)  
- Dashboard **Streamlit** avec filtres (style “app”)
"""
)

st.info("Prochaine étape : va sur **Overview** dans le menu à gauche.")
