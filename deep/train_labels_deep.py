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
