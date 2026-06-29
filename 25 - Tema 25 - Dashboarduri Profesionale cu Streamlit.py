import streamlit as st
import pandas as pd
import plotly.express as px


# Titlu aplicatie

st.title("Dashboard Clienti si Produse")


# ==============================
# DATE CLIENTI
# ==============================

clienti = pd.DataFrame({
    "Nume": ["Ana", "Ion", "Maria", "Dan", "Elena"],
    "Oras": ["Timisoara", "Cluj", "Bucuresti", "Iasi", "Brasov"],
    "Varsta": [25, 40, 32, 28, 36],
    "Venit": [4000, 6500, 5200, 4800, 7000],
    "Achizitii": [5, 8, 6, 4, 9]
})


st.subheader("Lista clienti")

st.dataframe(clienti)


# ==============================
# GRAFIC CORELATIE VARSTA / VENIT
# ==============================

st.subheader("Corelatie Varsta - Venit")

fig = px.scatter(
    clienti,
    x="Varsta",
    y="Venit",
    size="Achizitii",
    hover_name="Nume",
    title="Corelatia dintre varsta si venit"
)

st.plotly_chart(fig)


# ==============================
# DATE PRODUSE
# ==============================

produse = pd.DataFrame({
    "Produs": ["Laptop", "Telefon", "Mouse", "Monitor", "Tastatura"],
    "Pret": [4000, 2500, 150, 900, 300],
    "Cantitate": [5, 10, 20, 7, 12]
})


# calcul vanzari totale

produse["Vanzari_totale"] = produse["Pret"] * produse["Cantitate"]


st.subheader("Date produse")

st.dataframe(produse)


# ==============================
# GRAFIC VANZARI PRODUSE
# ==============================

fig2 = px.bar(
    produse,
    x="Produs",
    y="Vanzari_totale",
    title="Vanzari totale pe produs"
)

st.plotly_chart(fig2)

