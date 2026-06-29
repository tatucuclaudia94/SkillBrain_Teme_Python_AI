import streamlit as st
import joblib
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# dataset simulare medicala

X = np.array([

[22,0,120],
[35,1,140],
[29,0,130],
[41,1,150],
[19,0,110],
[37,1,145],
[28,0,125],
[39,1,148]

])

y = np.array([

0,
2,
1,
2,
0,
2,
1,
2

])


# split dataset

X_train, X_test, y_train, y_test = train_test_split(

X,
y,
test_size=0.2,
random_state=42

)


# model AI

model = RandomForestClassifier()

model.fit(X_train,y_train)


# salvare model

joblib.dump(model,"model_sarcina.pkl")


# incarcare model

model = joblib.load("model_sarcina.pkl")


# interfata Streamlit

st.title("AI Predictie risc sarcina")

st.write("Aplicatie demonstrativa pentru obstetrica si ginecologie")


varsta = st.number_input(

"Varsta mamei",
18,
50

)

diabet = st.slider(

"Diabet gestational (0=Nu, 1=Da)",
0,
1

)

tensiune = st.number_input(

"Tensiune arteriala",
90,
180

)


if st.button("Calculeaza risc"):

    pred = model.predict([[varsta,diabet,tensiune]])

    clase = [

    "Risc scazut",
    "Risc mediu",
    "Risc ridicat"

    ]

    rezultat = clase[pred[0]]

    st.success(f"Rezultat: {rezultat}")



