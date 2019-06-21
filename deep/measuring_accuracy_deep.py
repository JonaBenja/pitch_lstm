# measuring_accuracy for lstm1 and lstm2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import Model as model
from keras.models import load_model

import train_data_deep
train_data = train_data_deep.train_data_deep

import train_labels_deep
train_labels = train_labels_deep.train_labels_deep_acc

test_data = train_data[:21211]
test_data_m = train_data[-21211:]

for elem in test_data_m:
    test_data.append(elem)

print(len(test_data))

test_labels = train_labels[:21211]
test_labels_m = train_labels[-21211:]

for elem in test_labels_m:
    test_labels.append(elem)

train_data = train_data[21211:-21211]
train_labels = train_labels[21211:-21211]

test_data1 = np.array(test_data)

model = load_model('../models/deep.h5')
prediction = model.predict(test_data1, batch_size = 42422)
prediction = prediction.tolist()

total_frames = 0
num_sound = 0
errors = 0

# measure accuracy like network does on test set
for frame in prediction:
    total_frames += 1
    node = frame.index(max(frame))
    label = test_labels[total_frames-1]
    if node != label[0]:
        errors += 1

print("Total frames:", total_frames)
print("Errors:", errors)
print("Accuracy:", (total_frames - errors) / total_frames)


COR = 1
if len(test_data[0]) == 30:
    COR = 0
elif len(test_data[0]) == 28:
    COR = 1

test_frames = 0
gross_errors_freq = 0
gross_errors_node = 0
gross_errors_voicing = 0
too_high = 0
too_low = 0
voiceless = 0
voiced = 0

# measure error percentage like YIN does
for frame in prediction:
    test_frames += 1
    node = frame.index(max(frame))
    label = test_labels[test_frames-1]

    # voiced
    if label[0] != 0:
        if node == 0:
            voiceless += 1
        else:
            candidate = test_data[test_frames-1][node-COR]*100
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
print("The number of too high gross errors is: ", too_high)
print("The number of too low gross errors is: ", too_low)
print("The number of wrong voiceless gross errors is: ", too_high)
print("The number of wrong voiced errors is: ", too_low)
print("The number of gross errors freq is: ", gross_errors_freq)
print("The number of gross errors voicing is: ", gross_errors_voicing)
print("The percentage of gross errors voicing is: ", round(gross_errors_voicing/test_frames*100, 2), "%")
print("The percentage of wrong voiced gross errors is: ", round(voiced/gross_errors_voicing*100, 2), "%")
print("The percentage of wrong voiceless gross errors is: ", round(voiceless/gross_errors_voicing*100, 2), "%")
print("The percentage of gross errors freq is: ", round(gross_errors_freq/test_frames*100, 2), "%")
print("The percentage of too high gross errors is: ", round(too_high/gross_errors_freq*100, 2), "%")
print("The percentage of too low gross errors is: ", round(too_low/gross_errors_freq*100, 2), "%")
print("The percentage of (all) gross errors is: ", round(gross_errors/test_frames*100, 2), "%")
print("The accuracy is: ", round(100-(gross_errors/test_frames*100), 2), "%")
