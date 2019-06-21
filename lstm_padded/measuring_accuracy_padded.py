# measuring_accuracy for lstm1 and lstm2

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import Model as model
from keras.models import load_model

import train_data_padded
import train_labels_padded

train_data = train_data_padded.train_data_padded
train_labels = train_labels_padded.train_labels_padded_acc

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

test_data = np.array(test_data).reshape(168, 447, 28)

model = load_model('../models/blstm_padded.h5')

prediction = model.predict(test_data, batch_size = 168).tolist()

print(len(prediction))
print(len(test_labels))

# measure accuracy like network does on test set
COR = 1

if len(train_data[0][0]) == 30:
    COR = 0
elif len(train_data[0][0]) == 28:
    COR = 1

total_frames = 0
num_sound = 0
errors = 0
pad_sound = [   0., 0., 0., 0., 0., 0.,
                0., 0., 0., 0., 0., 0.,
                0., 0., 0., 0., 0., 0.,
                0., 0., 0., 0., 0., 0.,
                0., 0., 0., 0.]

for sound in prediction:
    num_sound += 1
    num_frame = 0
    for frame in sound:
        num_frame += 1
        label = test_labels[num_sound-1][num_frame-1]
        if label != [0.0, 0.0]:
            total_frames += 1
            node = frame.index(max(frame))
            if node != label[0]-1:
                errors += 1

print("Total frames:", total_frames)
print("Errors:", errors)
print("Accuracy:", (total_frames - errors) / total_frames)

num_sound = 0
test_frames = 0
gross_errors_freq = 0
gross_errors_node = 0
gross_errors_voicing = 0
too_high = 0
too_low = 0
voiceless = 0
voiced = 0

# measure error percentage like YIN does
for sound in prediction:
    num_sound += 1
    num_frame = 0
    for frame in sound:
        num_frame += 1
        label = test_labels[num_sound-1][num_frame-1]
        if label != [0.0, 0.0]:
            test_frames += 1
            node = frame.index(max(frame))

            # voiced
            if label[0]-1 != 0:
                if node == 0:
                    voiceless += 1
                else:
                    candidate = (test_data[num_sound-1][num_frame-1][node-COR]*100)
                    if abs(candidate - label[1]) / label[1] > 0.2:
                        if candidate > label[1]:
                            too_high += 1
                        else:
                            too_low += 1
            # voiceless
            else:
                if node != 0:
                    voiced += 1

gross_errors_freq = too_high + too_low
gross_errors_voicing = voiceless + voiced
gross_errors = gross_errors_freq + gross_errors_voicing

print("The number of test frames is: ", test_frames)
print("The number of gross errors is: ", gross_errors)
print("The number of gross errors freq is: ", gross_errors_freq)
print("The number of too high gross errors is: ", too_high)
print("The number of too low gross errors is: ", too_low)
print("The number of gross errors voicing is: ", gross_errors_voicing)
print("The number of wrong voiced errors is: ", voiced)
print("The number of wrong voiceless errors is: ", voiceless)
print("The percentage of gross errors voicing is: ", round(gross_errors_voicing/test_frames*100, 2), "%")
print("The percentage of wrong voiced gross errors is: ", round(voiced/gross_errors_voicing*100, 2), "%")
print("The percentage of wrong voiceless gross errors is: ", round(voiceless/gross_errors_voicing*100, 2), "%")
print("The percentage of gross errors freq is: ", round(gross_errors_freq/test_frames*100, 2), "%")
print("The percentage of too high gross errors is: ", round(too_high/gross_errors_freq*100, 2), "%")
print("The percentage of too low gross errors is: ", round(too_low/gross_errors_freq*100, 2), "%")
print("The percentage of (all) gross errors is: ", round(gross_errors/test_frames*100, 2), "%")
print("The accuracy is: ", round(100-(gross_errors/test_frames*100), 2), "%")
