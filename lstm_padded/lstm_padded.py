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
from keras import regularizers
from keras.callbacks import ModelCheckpoint
import numpy as np
from numpy  import array
import argparse

import train_data_padded
train_data = train_data_padded.train_data_padded

import train_labels_padded
train_labels = train_labels_padded.train_labels_padded

# train data = 840 sounds, 375480 frames
# test data = 0.20 * 840 = 168 sounds, 75096 frames, 37548 per kant
# train data = 672 sounds, 300384 frames
# validation data = 0.20 * 840 = 134 sounds, 59898 frames, 29949 per kant
# train data = 538 sounds, 240486 frames.

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

train_data = np.array(train_data)
train_labels = np.array(train_labels)
test_data = np.array(test_data)
test_labels = np.array(test_labels)

train_data = train_data.reshape(672, 447, 28)
train_labels = train_labels.reshape(672, 447, 15)
test_data = test_data.reshape(168, 447, 28)
test_labels = test_labels.reshape(168, 447, 15)


mask1 = [   0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0.]

model = Sequential([

    Masking(mask_value = mask1, input_shape = (447, 28)),

    Bidirectional(LSTM(96,
        return_sequences = True,
        recurrent_activation = 'sigmoid',
        input_shape = (447, 28))),

    Bidirectional(LSTM(96,
        return_sequences = True,
        recurrent_activation = 'sigmoid',
        input_shape = (447, 28))),

    Dense(15, activation = tf.keras.activations.softmax),

    ])

model.compile(  loss = 'categorical_crossentropy',
                optimizer = 'Adam',
                metrics = ['accuracy'])

model.summary()

model.fit(  train_data,
            train_labels,
            epochs = 115,
            batch_size = 256,
            validation_data = (test_data, test_labels),
            verbose = 1)
results1 = model.evaluate(test_data, test_labels)
print(results1)

model.save('../models/blstm_padded.h5')
