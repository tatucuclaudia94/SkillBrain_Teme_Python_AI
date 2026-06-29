import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime


# conectare baza de date

conn = sqlite3.connect("raport.db", check_same_thread=False)
cursor = conn.cursor()


# creare tabel daca nu exista

cursor.execute(
"CREATE TABLE IF NOT EXISTS raport(id INTEGER PRIMARY KEY AUTOINCREMENT, nume TEXT, valoare INTEGER, data_salvare TEXT)"
)

conn.commit()


# titlu aplicatie

st.title("Dashboard Raport")


# introducere date

st.subheader("Adauga raport")

nume = st.text_input("Nume")
valoare = st.number_input("Valoare", 0, 10000)


# salvare date

if st.button("Salveaza"):

    data = datetime.now().strftime("%Y-%m-%d")

    # protectie SQL Injection

    cursor.execute(
    "INSERT INTO raport (nume, valoare, data_salvare) VALUES (?, ?, ?)",
    (nume, valoare, data)
    )

    conn.commit()

    st.success("Date salvate")


# citire date

df = pd.read_sql_query("SELECT * FROM raport", conn)

st.subheader("Date salvate")

st.dataframe(df)


# filtrare luna / an

st.subheader("Filtrare dupa data")

if not df.empty:

    df["data_salvare"] = pd.to_datetime(df["data_salvare"])

    an = st.selectbox("Selecteaza anul", df["data_salvare"].dt.year.unique())

    luna = st.selectbox("Selecteaza luna", df["data_salvare"].dt.month.unique())

    filtrat = df[
    (df["data_salvare"].dt.year == an) &
    (df["data_salvare"].dt.month == luna)
    ]

    st.dataframe(filtrat)


# stergere linie

st.subheader("Stergere raport")

id_sters = st.number_input("ID raport de sters", 0)

if st.button("Sterge"):

    cursor.execute(
    "DELETE FROM raport WHERE id=?",
    (id_sters,)
    )

    conn.commit()

    st.success("Raport sters")
    

