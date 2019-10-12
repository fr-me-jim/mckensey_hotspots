import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
#load data



dc = pd.read_csv('./dc2.csv')


print(dc.info())
#Neural Network
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical
import keras

X = dc.drop('target', axis = 1)
Y = dc.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
accuracies = []
losses = []
for i in range(0, 1):
    model = Sequential()
    model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(5, input_dim=10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.
    model.fit(X_train, Y_train, epochs=30, batch_size=32, verbose=1)
    loss, acc = model.evaluate(X_test, Y_test, batch_size=32)
    for j in range(0,len(X),5):
        print(model.predict(X[j:j+5]))
        print(Y[j:j+5])

