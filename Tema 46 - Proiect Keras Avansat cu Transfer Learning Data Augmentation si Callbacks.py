import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ReduceLROnPlateau
import matplotlib.pyplot as plt


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

    "dataset_cafenele",

    target_size=(224,224),

    batch_size=32,

    subset="training"

)

val_data = datagen.flow_from_directory(

    "dataset_cafenele",

    target_size=(224,224),

    batch_size=32,

    subset="validation"

)


# transfer learning EfficientNet

base_model = tf.keras.applications.EfficientNetB0(

    weights="imagenet",

    include_top=False,

    input_shape=(224,224,3)

)

base_model.trainable = False


# model

model = Sequential()

model.add(base_model)

model.add(GlobalAveragePooling2D())

model.add(Dense(128,activation="relu"))

model.add(Dropout(0.4))

# 4 clase

model.add(Dense(4,activation="softmax"))


# compilare model

model.compile(

    optimizer="adam",

    loss="categorical_crossentropy",

    metrics=["accuracy"]

)


# reduce learning rate

reduce_lr = ReduceLROnPlateau(

    monitor="val_loss",

    factor=0.2,

    patience=3,

    min_lr=0.00001

)


# antrenare model

history = model.fit(

    train_data,

    validation_data=val_data,

    epochs=10,

    callbacks=[reduce_lr]

)


# grafic acuratete

plt.plot(history.history["accuracy"])

plt.plot(history.history["val_accuracy"])

plt.title("Evolutia acuratetii")

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.legend(["train","validation"])

plt.show()

