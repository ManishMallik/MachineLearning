# -*- coding: utf-8 -*-
"""part1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m4aXhJ0seROjo74kPIq_Wy-Uxerv4BWT

Will need data processing beforehand
"""

#1st part: Multivariate Linear Regression built manually (no libraries for this and gradient descent)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score

"""Predict"""

#Predict function
def predict(X, w):
    #w[0] would be considered the bias as it's corresponding x value is 1
    return np.dot(X, w[1:]) + w[0]

"""MSE loss funct"""

#MSE Function
def mse_loss_funct(y_pred, y_act):
    # formula for MSE
    return np.mean((y_pred - y_act) ** 2)

"""SSR and Gradient Descent Functions"""

#SSR function/formula
def ssr_gradient(X, y, w):
    m = len(y)
    res = np.dot(X, w) - y
    gradient = 1 / m * (np.dot(X.T, res))
    return gradient

#Gradient descent function (elaborated from the lab to fit for multivariate linear regression)
def gradient_descent(
     gradient, x, y, start, learn_rate, n_iter, tolerance=1e-08
 ):
  cost_history = [1e10]
  #vector of weights
  vector = start
  for _ in range(n_iter):
    #Calculate the cost for each iteration
    err = np.dot(x, vector) - y
    cost = 1/(2*len(y)) * np.dot(err.T, err)

    #keep track of each cost for the plot later on
    cost_history.append(cost)

    #Do the gradient descent and update the vector containing weights
    derivative = gradient(x, y, vector)
    diff = -learn_rate * derivative

    #Can leave function if tolerance is achieved
    if np.all(np.abs(diff) <= tolerance):
      break
    vector += diff
  cost_history.pop(0)
  return vector, cost_history

"""Choosing the features (we will use 6 features: horsepower and car name not included)"""

#Main code as follows
#correlation analysis
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
column_names = ["MPG", "Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration", "Model Year", "Origin", "Car Name"]
data = pd.read_csv(url, names=column_names, delim_whitespace=True)
data = data.sample(frac=1)

#Getting the data of the 6 feature attributes we chose
X = data[['Cylinders', 'Displacement', 'Weight', 'Acceleration', 'Model Year', 'Origin']]
#Getting the data of the target attribute: MPG
y = data['MPG']

#Randomly split the dataset into training set(80%) and testing set(20%)
rows = data.shape[0]
ratio = 0.8
index = int(rows * ratio)
X_train = X[0:index]
y_train = y[0:index]
X_test = X[index:]
y_test = y[index:]
X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)

"""Training the model and Testing it"""

#Training
learning_rate = 0.0000001
num_iter = 1000000
start_weights=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

#x[0] should be one to account for w[0], the bias
X_adjusted = np.column_stack((np.ones((X_train.shape[0], 1)), X_train))
weights, costs = gradient_descent(
    ssr_gradient, X_adjusted, y_train, start_weights, learning_rate, num_iter
)

print(f"Weight coefficients: {weights}")

hypothesis_train = predict(X_train, weights)
mse = mse_loss_funct(hypothesis_train, y_train)
print(f"MSE Train: {mse}")
print(f"R^2 Coefficient for Training: {r2_score(y_train, hypothesis_train)}")
print(f"Explained Variance Score for Training: {explained_variance_score(y_train, hypothesis_train)}")

#Testing
hypothesis_test = predict(X_test, weights)
mse = mse_loss_funct(hypothesis_test, y_test)
print(f"MSE Test: {mse}")
print(f"R^2 Coefficient for Testing: {r2_score(y_test, hypothesis_test)}")
print(f"Explained Variance Score for Testing: {explained_variance_score(y_test, hypothesis_test)}")

#Plot the MSE vs Iterations Graph
x = np.arange(1, len(costs) + 1)
plt.plot(x, costs, "r", scalex=1000, scaley=2)
plt.title('MSE vs Iterations', size = 30 )
plt.xlabel('No. of iterations', size = 20)
plt.ylabel('MSE', size=20)
plt.show()

"""Plots of how each feature chosen relates to the output attributes"""

#Plotting different graphs for each attribute and compare its correlation to the target attribute
cols = ['Cylinders', 'Displacement', 'Weight', 'Acceleration', 'Model Year', 'Origin', 'MPG']
X_train_df = pd.DataFrame(X_train, columns=cols[:-1])

# input and output
fig, axs = plt.subplots(1, len(cols) - 1, figsize=(20, 5))

x_labels = cols[:-1]

for i, subp in enumerate(axs):
    x_vals = X_train_df[x_labels[i]]
    subp.scatter(x_vals, y_train, alpha=0.5)
    subp.set_xlabel(x_labels[i])
    subp.set_ylabel('MPG')

plt.tight_layout()
plt.show()