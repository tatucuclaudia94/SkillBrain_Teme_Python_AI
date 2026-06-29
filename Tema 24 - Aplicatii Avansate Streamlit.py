import streamlit as st
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


# Titlu aplicatie

st.title("Predictie scor test")


# Generare dataset pentru antrenare

np.random.seed(0)

ore_studiu = np.random.randint(1, 10, 50)

scor = ore_studiu * 10 + np.random.randint(-5, 5, 50)


df = pd.DataFrame({
    "Ore_studiu": ore_studiu,
    "Scor_test": scor
})


# Antrenare model ML

X = df[["Ore_studiu"]]

y = df["Scor_test"]

model = LinearRegression()

model.fit(X, y)


# Slider pentru ore de studiu

ore = st.slider("Ore de studiu", 1, 12, 5)


# Predictie

predictie = model.predict([[ore]])


st.write("Scor estimat:", int(predictie[0]))


# Vizualizare dataset

st.subheader("Date folosite pentru antrenare")

st.dataframe(df)


# Upload fisier

st.subheader("Upload fisier pentru analiza")

fisier = st.file_uploader("Incarca un CSV", type=["csv"])


if fisier is not None:

    df_upload = pd.read_csv(fisier)

    st.write("Datele incarcate:")

    st.dataframe(df_upload)

