import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# incarcare dataset
iris = load_iris()

X = iris.data
y = iris.target


# impartire train test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)


# scalare date
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


# creare model tensorflow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")
])


# compilare model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# antrenare model
model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=8,
    validation_split=0.2
)


# predictii
pred = model.predict(X_test)

pred = pred.argmax(axis=1)


# acuratete
acc = accuracy_score(y_test, pred)

print("Accuracy:", acc)
