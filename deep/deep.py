#Deep network
from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Embedding, Dropout, TimeDistributed
from keras.layers import LSTM
from keras.optimizers import Adam, SGD
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint

import numpy as np
from numpy import array

import train_data_deep
train_data = train_data_deep.train_data_deep

import train_labels_deep
train_labels = train_labels_deep.train_labels_deep

test_data = train_data[:21211]
test_data_m = train_data[-21211:]

for elem in test_data_m:
    test_data.append(elem)

test_labels = train_labels[:21211]
test_labels_m = train_labels[-21211:]

for elem in test_labels_m:
    test_labels.append(elem)

train_data = train_data[21211:-21211]
train_labels = train_labels[21211:-21211]

train_data = array(train_data)
train_labels = array(train_labels)
test_data = array(test_data)
test_labels = array(test_labels)

print(len(train_data), len(train_labels))

model = Sequential([

    Dense(28, activation = tf.keras.activations.relu),

    Dense(1000, activation = tf.keras.activations.relu),

    Dense(15, activation = tf.keras.activations.softmax)
  ])


model.compile(optimizer = 'Adam',
                loss = 'categorical_crossentropy',
                metrics=['accuracy'])

history = model.fit(
            train_data,
            train_labels,
            epochs = 115,
            batch_size = 128,
            validation_data = (test_data, test_labels),
            verbose = 1)

model.summary()

print(model.evaluate(test_data, test_labels))

model.save('models/deep.h5')
