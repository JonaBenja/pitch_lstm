import csv
import numpy as np

train_labels_padded = []
count = 0
n_frames = 0
pad = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
pad_acc = [0., 0.]
sound = []
sound_acc = []
train_labels_padded_acc = []

with open('../train_labels_all') as csvfile:
    first_frame = csv.reader(csvfile, delimiter='\t')
    for row in first_frame:
        count += 1
        if count > 1:
            if row == ['eos', 'eos']:
                pad_value = 447 - n_frames

                for j in range(0, pad_value):
                    sound.append(pad)
                    sound_acc.append(pad_acc)

                train_labels_padded.append(sound)
                train_labels_padded_acc.append(sound_acc)

                sound = []
                sound_acc = []
                n_frames = 0

            else:
                n_frames += 1
                frame = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                frame_acc = [0, 0]
                place = int(row[0]) -1
                frame[place] = 1
                frame_acc[0] = place
                frame_acc[1] = float(row[1])
                sound.append(frame)
                sound_acc.append(frame_acc)
