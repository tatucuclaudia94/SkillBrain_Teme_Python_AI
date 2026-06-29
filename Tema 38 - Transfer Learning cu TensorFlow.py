import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models


# incarcare dataset personal (exemplu cu imagini din folder)

dataset = tf.keras.preprocessing.image_dataset_from_directory(
"dataset",
image_size=(224,224),
batch_size=32
)


# incarcare model ResNet50

base_model = tf.keras.applications.ResNet50(
weights="imagenet",
include_top=False,
input_shape=(224,224,3)
)


# blocare straturi model baza

base_model.trainable = False


# creare model nou

model = models.Sequential()

model.add(base_model)

model.add(layers.GlobalAveragePooling2D())

model.add(layers.Dense(128, activation="relu"))

model.add(layers.Dense(10, activation="softmax"))


# compilare model

model.compile(
optimizer="adam",
loss="sparse_categorical_crossentropy",
metrics=["accuracy"]
)


# antrenare model

model.fit(
dataset,
epochs=5
)


# fine tuning ultime straturi

base_model.trainable = True


for layer in base_model.layers[:-20]:
    layer.trainable = False


# recompilare model

model.compile(
optimizer=tf.keras.optimizers.Adam(1e-5),
loss="sparse_categorical_crossentropy",
metrics=["accuracy"]
)


# antrenare dupa fine tuning

model.fit(
dataset,
epochs=5
)

