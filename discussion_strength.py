import numpy as np

import train_data_deep
train_data = train_data_deep.train_data_deep

import train_labels_deep
train_labels = train_labels_deep.train_labels_deep_acc

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

test_frames = 0
count = 0
count_pb = 0

for frame in test_data:
    test_frames += 1
    label = test_labels[test_frames-1]
    candidates = train_data[test_frames-1][0:13]
    if label[0] != 0:
        i_strength = label[0]
        i_max_strength = frame.index(min(frame[14:27]))
        if i_max_strength != i_strength:
            count += 1
            if candidates[i_max_strength] > 600 or candidates[i_max_strength] < 75:
                count_pb += 1

print("Test frames:", test_frames)
print("Count:", count)
print("Percentage:", count/test_frames*100)
print("Countpb:", count_pb)
print("Percentage:", count_pb/test_frames*100)
