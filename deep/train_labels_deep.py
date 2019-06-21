import csv
import numpy as np

train_labels_deep = []
train_labels_deep_acc = []
frame = []
count = 0


with open('../train_labels_all') as csvfile:
    first_frame = csv.reader(csvfile, delimiter='\t')
    for row in first_frame:
        count += 1
        if count > 1:
            if row != ['eos', 'eos'] and row != ['eof', 'eof'] and row != ['0', '0']:
                frame = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                frame_acc = [0, 0]
                place = int(row[0]) - 1
                frame[place] = 1
                frame_acc[0] = place
                frame_acc[1] = float(row[1])
                train_labels_deep.append(frame)
                train_labels_deep_acc.append(frame_acc)

values = 0
voiced_values = 0
for frame in train_labels_deep:
    values += 1
    if frame[0] == 1:
        voiced_values += 1

print("Values:", values)
print("Voiced values:", voiced_values)
