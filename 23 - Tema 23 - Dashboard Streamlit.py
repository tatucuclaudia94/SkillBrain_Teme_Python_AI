import streamlit as st
import pandas as pd
import numpy as np


# Titlu aplicatie

st.title("Dashboard Angajati")


# Creeaza date pentru angajati

df = pd.DataFrame({
    "Nume": ["Ana", "Ion", "Maria", "Dan", "Elena", "Paul", "Andrei"],
    "Departament": ["IT", "HR", "IT", "Marketing", "HR", "IT", "Marketing"],
    "Salariu": [5000, 4200, 6500, 4800, 3900, 7200, 4600],
    "Varsta": [25, 32, 29, 41, 27, 35, 38]
})


# Tabs pentru diferite analize

tab1, tab2, tab3 = st.tabs(["Date Angajati", "Filtrare Salarii", "Salarii peste medie"])


# Tab 1 - Afisare date

with tab1:

    st.subheader("Tabel angajati")

    st.dataframe(df)


# Tab 2 - Slider interval salariu

with tab2:

    st.subheader("Filtrare salarii")

    min_sal = int(df["Salariu"].min())
    max_sal = int(df["Salariu"].max())

    interval = st.slider("Alege interval salariu", min_sal, max_sal, (min_sal, max_sal))

    filtrat = df[(df["Salariu"] >= interval[0]) & (df["Salariu"] <= interval[1])]

    st.dataframe(filtrat)


    # Salvare CSV

    csv = filtrat.to_csv(index=False)

    st.download_button(
        label="Descarca CSV",
        data=csv,
        file_name="angajati_filtrati.csv",
        mime="text/csv"
    )


# Tab 3 - Salarii peste media totala

with tab3:

    st.subheader("Angajati cu salariu peste media totala")

    media = df["Salariu"].mean()

    peste_medie = df[df["Salariu"] > media]

    st.write("Media salariilor:", media)

    st.dataframe(peste_medie)

