# LSTM-network
from __future__ import absolute_import, division, print_function
import collections
import os

#-mpip install matplotlib

import tensorflow as tf
#K.set_image_data_format('channels_last')
from tensorflow import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Embedding, Dropout, TimeDistributed
from keras.layers import LSTM, Bidirectional, Masking, GRU
from keras.optimizers import Adam, SGD
from keras.utils import to_categorical
from keras import callbacks
from keras.callbacks import ModelCheckpoint
import numpy as np
from numpy  import array
import argparse

import train_data_batch1
train_data = train_data_batch1.train_data_batch1

import train_labels_batch1
train_labels = train_labels_batch1.train_labels_batch1

test_data = train_data[:84]
test_data_m = train_data[-84:]

for elem in test_data_m:
    test_data.append(elem)

test_labels = train_labels[:84]
test_labels_m = train_labels[-84:]

for elem in test_labels_m:
    test_labels.append(elem)

train_data = train_data[84:-84]
train_labels = train_labels[84:-84]


train_data1 = []
for sound in train_data:
    sound = np.array(sound).reshape(1, len(sound), 28)
    train_data1.append(sound)

train_labels1 = []
for sound in train_labels:
    sound = np.array(sound).reshape(1, len(sound), 15)
    train_labels1.append(sound)

test_data1 = []
for sound in test_data:
    sound = np.array(sound).reshape(1, len(sound), 28)
    test_data1.append(sound)

test_labels1 = []
for sound in test_labels:
    sound = np.array(sound).reshape(1, len(sound), 15)
    test_labels1.append(sound)

model = Sequential([

    Bidirectional(LSTM(96,
        return_sequences = True,
        stateful = True,
        recurrent_activation = 'sigmoid'),
        batch_input_shape = (1, None, 28)),

    Bidirectional(LSTM(96,
        return_sequences = True,
        stateful = True,
        recurrent_activation = 'sigmoid')),

    Dense(15, activation = tf.keras.activations.softmax),

    ])

model.compile(  loss = 'categorical_crossentropy',
                optimizer = 'Adam',
                metrics = ['accuracy'])

model.summary()

epochs = 115

for j in range(epochs):
    for i in range(len(train_data1)):
        print(j+1, "/", epochs)
        print(i+1, "/", len(train_data1))
        model.fit(  train_data1[i],
                    train_labels1[i],
                    epochs = 1,
                    batch_size = 1,
                    validation_data = (test_data1[57], test_labels1[57]),
                    verbose = 1)
    model.save('../models/blstm_batch1.h5')

model.save('../models/blstm_batch1.h5')

all_accuracy = 0
all_loss = 0
for i in range(len(test_data1)):
    results = model.test_on_batch(test_data1[i], test_labels1[i])
    all_loss += results[0]
    all_accuracy += results[1]

print("Loss:", all_loss/len(train_data1))
print("Accuracy:", all_accuracy/len(train_data1))
