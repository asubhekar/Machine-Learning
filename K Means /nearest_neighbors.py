# -*- coding: utf-8 -*-
"""Nearest_Neighbors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IUZbjdXrBeYOPXgZQy7LbKMj8-9uXDWk

# Nearest Neighbors Implementation

### Importing Libraries
"""

# preprocessing libraries
import pandas as pd
import numpy as np
# algorithm libraries
from sklearn.neighbors import KNeighborsClassifier
#Metrics libraries
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix

"""### Data Preprocessing"""

#importingt the training and testing data
X_train = pd.read_csv("train.csv")
X_test = pd.read_csv("test.csv")

y_train = X_train.iloc[:,-1]
y_test = X_test.iloc[:,-1]
X_train = X_train.drop(columns = ['class'])
X_test = X_test.drop(columns = ['actual-class','ID'])

"""### Classifying the data points in test.csv according to their 3-nearest neighbors."""

#Training the model with Manhattan Distance
manhattan = KNeighborsClassifier(n_neighbors = 3, p = 1)
manhattan.fit(X_train, y_train)

# Predicting the classes
y_pred_manhattan = manhattan.predict(X_test)

# Calculating the probability estimates for the final decision
manhattan.predict_proba(X_test)

"""### Classifying the data points in Test.csv according to their weighted 3-nearest neighbors (1/d^2)"""

def weight_distance(distances):
    weight = []
    for i in distances:
        weight.append(1/(i**2))
    return weight

# Training the model with Euclidean Distance
euclidean = KNeighborsClassifier(n_neighbors = 3, weights = weight_distance)
euclidean.fit(X_train, y_train)

# Predicting Classes
y_pred_euclidean = euclidean.predict(X_test)

# Checking if the predicted labels are same while using Manhattan and Euclidean Distances
predictions = 0
for i in range(len(y_pred_euclidean)):
    if y_pred_euclidean[i] == y_pred_manhattan[i]:
        predictions+=1

if predictions == 1:
    print("Predictions using Euclidean and Manhattan are similar.")
else:
    print("Number of different predictions", len(y_pred_euclidean)-predictions)

"""### Construct the confusion matrix and calculate Accuracy, Precision, F-measure"""

m_confusion = confusion_matrix(y_test, y_pred_manhattan)
m_acc = accuracy_score(y_test, y_pred_manhattan)
m_prec = precision_score(y_test, y_pred_manhattan)
m_f1 = f1_score(y_test, y_pred_manhattan)

print("Confusion Matrix for Manhattan Distance = \n", m_confusion)
print("Accuracy Score for Manhattan Distance = \n", m_acc)
print("Precision Score for Manhattan Distance = \n", m_prec)
print("F1 Score for Manhattan Distance = \n", m_f1)

e_confusion = confusion_matrix(y_test, y_pred_euclidean)
e_acc = accuracy_score(y_test, y_pred_euclidean)
e_prec = precision_score(y_test, y_pred_euclidean)
e_f1 = f1_score(y_test, y_pred_euclidean)

print("Confusion Matrix for Euclidean Distance = \n", e_confusion)
print("Accuracy Score for Euclidean Distance = \n", e_acc)
print("Precision Score for Euclidean Distance = \n", e_prec)
print("F1 Score for Euclidean Distance = \n", e_f1)

"""### Final Conclusion

From this we can conclude that Manhattan distance has better accuracy for weighted distances.
"""