# PITCH LSTM
This repository contains the code for my bachelor thesis about pitch tracking with an LSTM neural network: "*Debiased Autocorrelation and a bidirectional LSTM network for pitch estimation of speech sounds (2019)*".


## STRUCTURE

```bash
pitch_lstm
│
├── deep
│   ├── deep.py
│   ├── measuring_accuracy_deep.py
│   ├── train_data_deep.py
│   └── train_labels_deep.py
│
├── lstm_padded
│   ├── lstm_padded.py
│   ├── measuring_accuracy_padded.py
│   ├── train_data_padded.py
│   └── train_labels_padded.py
│
├── lstm_batch1
│   ├── lstm_batch1.py
│   ├── measuring_accuracy_batch1.py
│   ├── train_data_batch1.py
│   └── train_labels_batch1.py
│
├── README.md
│
├── models
│   ├── blstm_batch1.h5
│   ├── blstm_padded.h5
│   └── deep.h5
│
├── YIN settings_acf.praat
│
├── measuring_accuracy.praat
│
├── train_data+train_labels.zip
│   ├── train_data
│   └── train_labels
│
└── train_data.praat
```

## CONTENT

### deep

`deep.py`

This file contains the code for the construction of the deep network.

`measuring_accuracy_deep.py`

This file contains the code of measuring the accuracy of the deep network on the test set.

`train_data_deep.py`

This file contains the code for converting the train_data dataset to a form that can be fed to the deep network in  
Python.

`train_labels_deep.py`

This file contains the code for converting the train_labels dataset to a form that can be fed to the deep network in
Python.   
     
### lstm_padded

This directory contains all the code used for the lstm_padded network. 

`lstm_padded.py`

 This file contains the code for the construction of the lstm_padded network.

`measuring_accuracy_padded.py`

 This file contains the code of measuring the accuracy of the lstm_padded network on the test set.

`train_data_padded.py`

 This file contains the code for converting the train_data dataset to a form that can be fed to the lstm_padded network in  
 Python.

`train_labels_padded.py`

 This file contains the code for converting the train_labels dataset to a form that can be fed to the lstm_padded network
 in Python.
     
### lstm_batch1

This directory contains all the code used for the lstm_batch1 network. 

`lstm_batch1.py`
 
 This file contains the code for the construction of the lstm_batch1 network.
 
`measuring_accuracy_batch1.py`

 This file contains the code of measuring the accuracy of the lstm_batch1 network on the test set.

`train_data_batch1.py`

 This file contains the code for converting the train_data dataset to a form that can be fed to the lstm_batch1 network in  
 Python.

`train_labels_batch1.py`

 This file contains the code for converting the train_labels dataset to a form that can be fed to the lstm_batch1 network
 in Python.
 
### README 
     
`README.md`

This is the file you are reading now.
     
### models

This directory contains the three trained networks.

`blstm_batch1.h5`, `blstm_padded.h5`, `deep.h5`

### Praat scripts and data

`YIN settings_acf.praat`

This file contains the code for the imitation of the evaluation of the debiased autocorrelation in Praat by de Cheveinge and Kawahara (2000). Code to be run in Praat.

`measuring_accuracy_praat.praat`

This file contains the code for the evaluation of the debiased autocorrelation in Praat on the test set of the database created by Atake et al (2000). Code to be run in Praat.

`train_data+train_labels.zip`

This zip-file contains the two datasets used to train the networks that were constructed in my thesis. 

`train_data_all`

 This file contains the data the networks were trained on, including the test data. 

`train_labels_all`

This file contains the labels that were used to fine tune the networks and the measure the accuracy of the networks and the debiased autocorrelation in Praat, for the train data and the test data.
    
`train_data.praat`

This file contains the code that generated the data for the train_data_all and train_labels_all files. These files were created from the database of Atake et al (2000). Code to be run in Praat.
