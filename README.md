# Machine Learning Assignment 2
We utilized Google Colab for this assignment. Attached below is the link to our Colab notebook containing the code for the programming part of assignment 2:
https://colab.research.google.com/drive/1gD7VO4gLuY_YWOXU8y7EjGi-SJIUsttR?usp=sharing

There are a total of 7 different coding cells in this notebook. Run each cell in order from top to bottom. The first cell will contain the whole main code, which creates a neural network model and outputs the training and testing accuracies for each activation function. The remaining 6 cells will generate graphs for comparing between the actual outputs of each example and the predicted outputs of each example.

This Neural Network Model uses the Breast Cancer Wisconsin dataset from the UCI ML repositories. This consists of 9 attributes (we will not count Code # as that has no correlation with predicting the output), and 1 output, which can represent two classes: benign tumors (2) or malign tumors (4). We have a preprocess method that converts those class values to 0 and 1, respectively. Our train/test ratio was 80% of the dataset will be used to train the neural betwork model while the remaining 20% will be used for testing the model.

Important note -> we retrieved the dataset by using this URL in our code: "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
