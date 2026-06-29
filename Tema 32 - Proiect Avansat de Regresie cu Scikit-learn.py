import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score


# creare dataset imobiliar

data = {
"suprafata":[50,60,70,80,90,100,110,120],
"etaj":[1,2,3,4,5,6,7,8],
"zona":[1,2,2,3,3,3,2,1],
"pret":[50000,60000,70000,85000,90000,100000,110000,120000]
}

df = pd.DataFrame(data)


# adaugare coloana numar_camere

df["numar_camere"] = [2,2,3,3,4,4,5,5]


# variabile input

X = df[["suprafata","etaj","zona","numar_camere"]]

y = df["pret"]


# impartire date

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2
)


# model RandomForest

rf = RandomForestRegressor()

rf.fit(X_train, y_train)

pred_rf = rf.predict(X_test)

score_rf = r2_score(y_test, pred_rf)

print("RandomForest R2:", score_rf)


# model GradientBoosting

gb = GradientBoostingRegressor()

gb.fit(X_train, y_train)

pred_gb = gb.predict(X_test)

score_gb = r2_score(y_test, pred_gb)

print("GradientBoosting R2:", score_gb)


# calcul pret pe metru patrat

df["pret_mp"] = df["pret"] / df["suprafata"]


# nou model pentru pret/mp

X = df[["suprafata","etaj","zona","numar_camere"]]

y = df["pret_mp"]


X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2
)


model_mp = GradientBoostingRegressor()

model_mp.fit(X_train, y_train)

pred_mp = model_mp.predict(X_test)

score_mp = r2_score(y_test, pred_mp)

print("Model pret/mp R2:", score_mp)

