# VND_banknotes_classification
- The funny application that can predict the VND banknote when the banknote is given as input by uploading and capturing frames from the webcam. 
- There are 9 denominations given for prediction: 1k, 2k, 5k, 10k, 20k, 50k, 100k, 200k, 500k.
- Data is provided from the Coder School and collected a little more by myself. They are splitted into trainning set and test set.
- The model used is DenseNet169 with the best score found is accuracy = 0.93. 
- Because camera is only allowed to open on the local, so that on the streamlit only inputting by uploading image works.
