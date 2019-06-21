import csv
import numpy as np

frequencies = []
strengths = []
train_data_padded = []
frame = []
sound = []
count = 0

pad_sound = [0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0., 0., 0.,
            0., 0., 0., 0.]


with open ('../train_data_all') as csvfile:
    first_frame = csv.reader(csvfile, delimiter='\t')
    for row in first_frame:
        count += 1
        if count > 1:
            if row == ['eof', 'eof']:
                pad_candidates = (14 - len(frequencies))

                for elem in frequencies:
                    frame.append(elem/100)
                for i in range(0, pad_candidates):
                    frame.append(0.)

                for elem in strengths:
                    frame.append(np.log(1-elem))
                for i in range(0, pad_candidates):
                    frame.append(0.)

                sound.append(frame)

                frequencies = []
                strengths = []
                frame = []
            elif row == ['eos', 'eos']:

                pad_sound_value = (447 - len(sound))
                for p in range(0, pad_sound_value):
                    sound.append(pad_sound)

                train_data_padded.append(sound)
                sound = []
            elif row != ['0', '0']:
                frequencies.append(float(row[0]))
                strengths.append(float(row[1]))
