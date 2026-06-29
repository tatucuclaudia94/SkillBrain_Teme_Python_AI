import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping

import numpy as np
from tensorflow.keras.preprocessing import image


# incarcare dataset cu dimensiune modificata

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "dataset_animale",
    image_size=(128,128),
    batch_size=32,
    validation_split=0.2,
    subset="training",
    seed=42
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "dataset_animale",
    image_size=(128,128),
    batch_size=32,
    validation_split=0.2,
    subset="validation",
    seed=42
)


# model CNN

model = Sequential()

model.add(Conv2D(32,(3,3),activation="relu",input_shape=(128,128,3)))
model.add(MaxPooling2D())

model.add(Conv2D(64,(3,3),activation="relu"))
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(128,activation="relu"))

# 3 clase -> clasificare multi-clasa

model.add(Dense(3,activation="softmax"))


# compilare model

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# early stopping

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5
)


# antrenare model

model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=20,
    callbacks=[early_stop]
)


# salvare model

model.save("model_animale.keras")


# script test imagine din PC

img = image.load_img("test.jpg", target_size=(128,128))

img_array = image.img_to_array(img)

img_array = np.expand_dims(img_array, axis=0)

pred = model.predict(img_array)

clase = ["alte_animale","corgi","rabbits"]

rezultat = clase[np.argmax(pred)]

print("Animal detectat:", rezultat)

