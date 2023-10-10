# Machine Learning Assignment 2
We utilized Google Colab for this assignment. Attached below is the link to our Colab notebook containing the code for the programming part of assignment 2:
https://colab.research.google.com/drive/1gD7VO4gLuY_YWOXU8y7EjGi-SJIUsttR?usp=sharing

There are a total of 14 different coding cells in this notebook. Run each cell in order from top to bottom. The first cell will contain the whole main code, which creates a neural network model and outputs the training and testing accuracies of each neural network using a different activation function. Additionally, it will print out the overall error for training and testing of each neural network with different activation functions. The remaining 13 cells will generate different types of graphs (brief descriptions/titles of each graph will be provided in text cells above the code cells containing the plot code).

This Neural Network Model uses the Breast Cancer Wisconsin dataset from the UCI ML repositories. This consists of 9 attributes (we will not count Code # as that has no correlation with predicting the output), and 1 output, which can represent two classes: benign tumors(2) or malign tumors(4). We have a preprocess method that converts those class values to 0 and 1, respectively. Our train/test ratio was 80% of the dataset will be used to train the neural betwork model while the remaining 20% will be used for testing the model.

The libraries we used are only for preprocessing the dataset, where we removed any rows containing missing values. We also imported numpy for the math, pd for getting the dataset, and matplotlib.pyplot for plotting the graphs. There were no libraries used for creating a neural network.

Our report of results in a tabular format, along with the summary of our results and all the graphs, are all in our assignment 2 report PDF file.

Important note: we retrieved the dataset by using this URL in our code: "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"

Assumptions we made: 
1. For each activation derivative function, the value being passed as a parameter (x) contains the output values of each hidden neuron and output neuron, which already went through the original activation function. Therefore, we do not have to call the respective original activation function when doing the derivative; instead, we do it in terms of x. For example, if x = sigmoid(some value), then in the sigmoid derivative function, we do x * (1-x) instead of sigmoid(x) * (1-sigmoid(x)), as we learned in our lecture.
2. There will not be a hidden neuron or output neuron with a neural net value (the value before going through the activation function) of 0. There is no value of 0 for the input values from the dataset that we are using. Additionally, we originally put some print statements to check the neural net of each hidden neuron and output neuron after each epoch, and we found some values that were close to 0, but we never came across an instance of exactly 0 for the net of each neuron. Therefore, we are making the assumption that each neuron will NOT have a net value of exactly 0, especially after going through many iterations, so there is no need to check if a net value of any neuron is exactly 0 while training a neural network with the ReLu function.
