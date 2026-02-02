import pandas as pd
import os
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Load Data and review content
iris_data = pd.read_csv("iris.csv")

print("\nLoaded Data: \n------------------")
print(iris_data.head())

#Use a label encoder to convert string to numeric values

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
iris_data['Species'] = label_encoder.fit_transform(iris_data['Species'])

#Convert input to numpy array
np_iris = iris_data.to_numpy()

#Seperate feature and target variables
X_data = np_iris[:,0:4]
Y_data=np_iris[:,4]

print("\nFeatures before scaling : \n--------------------")
print(X_data[:5,:])
print("\nTarget before scaling :\n---------------------")
print(Y_data[:5])

