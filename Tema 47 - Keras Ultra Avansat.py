import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# augmentare imagini

datagen = ImageDataGenerator(

    rescale=1./255,

    validation_split=0.2

)


# dataset

train_data = datagen.flow_from_directory(

    "dataset_hoteluri",

    target_size=(224,224),

    batch_size=32,

    subset="training"

)

val_data = datagen.flow_from_directory(

    "dataset_hoteluri",

    target_size=(224,224),

    batch_size=32,

    subset="validation"

)


# model pre-antrenat ResNet50

base_model = tf.keras.applications.ResNet50(

    weights="imagenet",

    include_top=False,

    input_shape=(224,224,3)

)

base_model.trainable = False


# model clasificare

model = Sequential()

model.add(base_model)

model.add(GlobalAveragePooling2D())

model.add(Dense(128,activation="relu"))

model.add(Dense(3,activation="softmax"))


# compilare

model.compile(

    optimizer="adam",

    loss="categorical_crossentropy",

    metrics=["accuracy"]

)


# antrenare

model.fit(

    train_data,

    validation_data=val_data,

    epochs=5

)


# salvare doar greutati

model.save_weights("hotel_weights.h5")

