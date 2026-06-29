import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models


# incarcare dataset Fashion-MNIST

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()


# normalizare imagini

X_train = X_train / 255.0
X_test = X_test / 255.0


# reshape pentru CNN

X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)


# creare model CNN

model = models.Sequential()

model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)))

model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64, (3,3), activation='relu'))

model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Flatten())

model.add(layers.Dense(128, activation='relu'))


# dropout pentru reducere overfitting

model.add(layers.Dropout(0.5))


# strat output

model.add(layers.Dense(10, activation='softmax'))


# compilare model

model.compile(
optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy']
)


# antrenare model

model.fit(
X_train,
y_train,
epochs=10,
validation_split=0.2
)


# evaluare model

loss, acc = model.evaluate(X_test, y_test)

print("Accuracy:", acc)

