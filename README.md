# KPI-Dashboard
KPI Dashboard “E-commerce”
# 📊 E-commerce KPI Dashboard – Data Analyst Portfolio Project

## 🎯 Objectif du projet
Ce projet a pour objectif de démontrer ma capacité à analyser des données business réelles et à produire un **dashboard décisionnel** permettant de suivre les performances d’une activité e-commerce.

Il couvre l’ensemble du cycle data :
- préparation et nettoyage des données
- modélisation et calcul des indicateurs
- restitution via un dashboard interactif orienté aide à la décision

---

## 🧩 Problématique métier
Comment suivre efficacement la performance commerciale d’une activité e-commerce ?

Questions adressées :
- Quel est le chiffre d’affaires global et son évolution dans le temps ?
- Quels sont les volumes de commandes et de clients ?
- Quelles catégories de produits performent le mieux ?
- Comment rendre ces informations accessibles aux décideurs ?

---

## 🛠️ Stack technique
- **Python** (pandas, numpy)
- **SQL** (SQLite)
- **Streamlit** (dashboard interactif)
- **Plotly** (visualisations)
- **SQLAlchemy** (connexion base de données)

---

## 🗂️ Données
Les données utilisées sont **simulées** à des fins pédagogiques, mais structurées de manière réaliste.

Tables :
- `customers` : clients (segment, ville, date d’inscription)
- `products` : produits (catégorie, prix)
- `orders` : transactions (dates, quantités, remises)

Certaines anomalies ont volontairement été introduites (valeurs manquantes) afin de refléter des problématiques de **qualité de données réelles**.

---

## 🔄 Pipeline de traitement
1. Génération des données brutes (CSV)
2. Chargement et modélisation dans une base **SQLite**
3. Calcul des KPI via requêtes **SQL**
4. Analyse et visualisation avec **pandas** et **Plotly**
5. Restitution via un dashboard **Streamlit**

---

## 📈 Indicateurs clés (KPI)
- Chiffre d’affaires
- Nombre de commandes
- Nombre de clients uniques
- Évolution mensuelle du chiffre d’affaires
- Répartition du CA par catégorie de produits

---

## 📊 Dashboard
Le dashboard permet :
- de filtrer les données par période
- de visualiser les tendances temporelles
- d’identifier les catégories les plus performantes
- d’accéder rapidement aux indicateurs clés pour la prise de décision

---

## 🚀 Lancer le projet en local
```bash
pip install -r requirements.txt
streamlit run app/app.py
