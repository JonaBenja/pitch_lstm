# PITCH LSTM
This repository contains code for my bachelor thesis about pitch tracking with a LSTM neural network.

## CONTENTS

* deep
This directory contains all the code used for the deep network. 

      * deep.py
      This file contains the code for the construction of the deep network.
   
      * discussion_strength.py
      This file contains the code used for measuring how many ground truth frames were not the candidate with the highest            strength. This number is treated in the discussion section of the paper.
   
      * measuring_accuracy_deep.py
      This file contains the code of measuring the accuracy of the deep network on the test set.
   
      * train_data_deep.py
      This file contains the code for converting the train_data dataset to a form that can be fed to the deep network in  
      Python.
   
      * train_labels_deep.py
      This file contains the code for converting the train_labels dataset to a form that can be fed to the deep network in
      Python.   

* YIN settings_acf.praat
This file contains the code for the imitation of the evaluation of the debiased autocorrelation in Praat de Cheveinge et al (2000). Code to be run in Praat.

* measuring_accuracy_praat.praat
This file contains the code for the evaluation of the debiased autocorrelation in Praat on the test set of the database created by Atake et al (2000). Code to be run in Praat.

* train_data+train_labels.zip
This zip-file contains the two datasets used to train the networks that were constructed in my thesis. 

    * train_data_all
    This contains the data the networks were trained on, including the test data. 
    
    * train_labels_all
    This contains the labels that were used to fine tune the networks and the measure the accuracy of the networks and the         debiased autocorrelation in Praat.
    
* train_data.praat
This file contains the code that generated the data for the train_data_all and train_labels_all files. These files were created from the database of Atake et al (2000).

