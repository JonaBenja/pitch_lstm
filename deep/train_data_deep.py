import csv
import numpy as np

frequencies = []
strengths = []
train_data_deep = []
frame = []
sound = []
count = 0


with open ('../train_data_all') as csvfile:
    first_frame = csv.reader(csvfile, delimiter='\t')
    for row in first_frame:
        count += 1
        if count > 1:
            if row == ['eof', 'eof']:
                pad = (14 - len(frequencies))
                #assert pad >= 0
                for elem in frequencies:
                    #frame.append(elem)
                    frame.append(elem/100)
                for i in range(0, pad):
                    frame.append(0.0)

                for elem in strengths:
                    #frame.append(elem)
                    frame.append(np.log(1-elem))
                for i in range(0, pad):
                    frame.append(0.0)

                train_data_deep.append(frame)

                frequencies = []
                strengths = []
                frame = []

            elif row != ['eos', 'eos'] and row != ['eof', 'eof'] and row != ['0', '0']:
                frequencies.append(float(row[0]))
                strengths.append(float(row[1]))
