import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import numpy as np


# augmentare imagini

datagen = ImageDataGenerator(

    rescale=1./255,

    rotation_range=20,

    zoom_range=0.2,

    horizontal_flip=True,

    validation_split=0.2

)


# incarcare dataset

train_data = datagen.flow_from_directory(

    "dataset_vacante",

    target_size=(224,224),

    batch_size=32,

    subset="training"

)

val_data = datagen.flow_from_directory(

    "dataset_vacante",

    target_size=(224,224),

    batch_size=32,

    subset="validation"

)


# transfer learning ResNet50

base_model = tf.keras.applications.ResNet50(

    weights="imagenet",

    include_top=False,

    input_shape=(224,224,3)

)

base_model.trainable = False


# model cu dropout

model = Sequential()

model.add(base_model)

model.add(GlobalAveragePooling2D())

model.add(Dense(128,activation="relu"))

model.add(Dropout(0.4))

model.add(Dense(3,activation="softmax"))


# compilare model

model.compile(

    optimizer="adam",

    loss="categorical_crossentropy",

    metrics=["accuracy"]

)


# antrenare model

model.fit(

    train_data,

    validation_data=val_data,

    epochs=10

)


# salvare model

model.save("model_vacante.keras")


# incarcare model

model_loaded = tf.keras.models.load_model(

    "model_vacante.keras"

)


# test imagine din PC

img = image.load_img(

    "test.jpg",

    target_size=(224,224)

)

img_array = image.img_to_array(img)

img_array = np.expand_dims(img_array, axis=0)

pred = model_loaded.predict(img_array)

clase = ["munte","oras","plaja"]

rezultat = clase[np.argmax(pred)]

print("Tip vacanta detectat:", rezultat)
