from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.utils import to_categorical


# incarcare dataset iris

iris = load_iris()

X = iris.data
y = iris.target


# impartire date iris

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# normalizare iris

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# conversie categorii iris

y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)


# model iris cu relu

model_relu = Sequential()

model_relu.add(Dense(64, activation="relu", input_shape=(4,)))
model_relu.add(Dropout(0.3))

model_relu.add(Dense(64, activation="relu"))
model_relu.add(Dropout(0.3))

model_relu.add(Dense(32, activation="relu"))

model_relu.add(Dense(3, activation="softmax"))


# compilare model relu

model_relu.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


# antrenare model relu

model_relu.fit(
    X_train,
    y_train_cat,
    epochs=50,
    verbose=0
)


# evaluare model relu

loss_relu, acc_relu = model_relu.evaluate(X_test, y_test_cat, verbose=0)

print("Accuracy Iris relu:", acc_relu)


# model iris cu tanh

model_tanh = Sequential()

model_tanh.add(Dense(64, activation="tanh", input_shape=(4,)))
model_tanh.add(Dropout(0.3))

model_tanh.add(Dense(64, activation="tanh"))
model_tanh.add(Dropout(0.3))

model_tanh.add(Dense(32, activation="tanh"))

model_tanh.add(Dense(3, activation="softmax"))


# compilare model tanh

model_tanh.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


# antrenare model tanh

model_tanh.fit(
    X_train,
    y_train_cat,
    epochs=50,
    verbose=0
)


# evaluare model tanh

loss_tanh, acc_tanh = model_tanh.evaluate(X_test, y_test_cat, verbose=0)

print("Accuracy Iris tanh:", acc_tanh)


# incarcare dataset wine

wine = load_wine()

Xw = wine.data
yw = wine.target


# impartire date wine

Xw_train, Xw_test, yw_train, yw_test = train_test_split(
    Xw, yw, test_size=0.2, random_state=42
)


# normalizare wine

scaler_wine = StandardScaler()

Xw_train = scaler_wine.fit_transform(Xw_train)
Xw_test = scaler_wine.transform(Xw_test)


# conversie categorii wine

yw_train_cat = to_categorical(yw_train)
yw_test_cat = to_categorical(yw_test)


# model wine

model_wine = Sequential()

model_wine.add(Dense(64, activation="tanh", input_shape=(13,)))
model_wine.add(Dropout(0.3))

model_wine.add(Dense(64, activation="tanh"))
model_wine.add(Dropout(0.3))

model_wine.add(Dense(32, activation="tanh"))

model_wine.add(Dense(3, activation="softmax"))


# compilare model wine

model_wine.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


# antrenare model wine

model_wine.fit(
    Xw_train,
    yw_train_cat,
    epochs=50,
    verbose=0
)


# evaluare model wine

loss_wine, acc_wine = model_wine.evaluate(Xw_test, yw_test_cat, verbose=0)

print("Accuracy Wine:", acc_wine)

