import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.regularizers import l2

import keras_tuner as kt


# dataset imagini

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "dataset_masini",
    image_size=(224,224),
    batch_size=32,
    validation_split=0.2,
    subset="training",
    seed=42
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "dataset_masini",
    image_size=(224,224),
    batch_size=32,
    validation_split=0.2,
    subset="validation",
    seed=42
)


# transfer learning MobileNet

base_model = tf.keras.applications.MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224,224,3)
)

base_model.trainable = False


# model cu Dropout si L2

model = Sequential()

model.add(base_model)

model.add(tf.keras.layers.GlobalAveragePooling2D())

model.add(Dense(128, activation="relu", kernel_regularizer=l2(0.01)))

model.add(Dropout(0.4))

model.add(Dense(2, activation="softmax"))


# compilare model

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# callbacks

early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5
)

checkpoint = ModelCheckpoint(
    "best_model.keras",
    monitor="val_loss",
    save_best_only=True
)

tensorboard = TensorBoard(
    log_dir="logs"
)


# antrenare

model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=20,
    callbacks=[early_stop, checkpoint, tensorboard]
)


# keras tuner pentru optimizare

def build_model(hp):

    model = Sequential()

    model.add(Dense(
        units=hp.Int("units", 64, 256, step=64),
        activation="relu"
    ))

    model.add(Dropout(
        hp.Float("dropout", 0.2, 0.5, step=0.1)
    ))

    model.add(Dense(2, activation="softmax"))

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


tuner = kt.RandomSearch(
    build_model,
    objective="val_accuracy",
    max_trials=5,
    directory="tuner",
    project_name="cars"
)


tuner.search(train_ds, validation_data=val_ds, epochs=5)

