import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
#load data
da = pd.read_csv('./Dataset/accidents.csv')


#print info from data
#print("accidents: \n \n \n")
print(da.info())


#print values from some colums
#print(da.target.value_counts())


#clean dataset
da.drop(labels = ['accident_id'], axis = 1, inplace = True)
da.drop(labels = ['lsoa_of_accident_location'], axis = 1, inplace = True)
#location_easting_osgr, location_northing_osgr


for i in da:
    d = []
    if i == "time":
        for j in range(0,len(da[i])):
            h = int(da[i][j].split(":")[0])
            #m = int(da[i][j].split(":")[1])
            d.append(h)
        da[i] = d
    elif i == "date":
        for j in range(0,len(da[i])):
            y = int(da[i][j].split("-")[0])
            m = int(da[i][j].split("-")[1])
            day = int(da[i][j].split("-")[2])
            d.append(dt.date(y,m,day).weekday())
        da[i] = d
    elif type(da[i][0]) is str:
        da.drop(i, axis = 1, inplace = True) #lol same accucary (look PC)
        #try:
        #    if da[i].value_counts()["-1"] < len(da[i]) * .05:
        #        #delete "-1"
        #        indexs = da.index[da[i] == "-1"].tolist()
        #        da.drop(indexs, axis = 0, inplace=True)
        #        print("Cleaned: " + i)
        #    else:
        #        #problematic colums too much "-1"
        #        if i == '2nd_road_class':
        #            print(da[i].value_counts())
        #            da[i] = da[i].replace("-1","Unclassified")
        #            print(da[i].value_counts())
        #        print("Ko: " + i)
        #except:
        #    print("No -1: "+ i)
        #temp_dummy = pd.get_dummies(da[i])
        #da = pd.concat([da,temp_dummy], axis = 1)
        #da.drop(i, axis = 1,inplace=True)

#Neural Network
from sklearn.model_selection import train_test_split
from keras.models import Sequential 
from keras.layers import Dense, Dropout 
from keras.utils import to_categorical 
import keras

X = da.drop('target', axis = 1)
print(X.info())
Y = da.target
print(Y.value_counts())
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10)  
accuracies = [] 
losses = [] 
for i in range(0, 5): 
    model = Sequential() 
    model.add(Dense(10, input_dim=X_train.shape[1], activation='relu')) 
    model.add(Dense(10, input_dim=10, activation='relu'))
    model.add(Dense(10, input_dim=10, activation='relu'))
    model.add(Dense(5, input_dim=10, activation='relu'))
    model.add(Dense(5, input_dim=5, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))   
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) 
    # x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.    
    model.fit(X_train, Y_train, epochs=5, batch_size=32, verbose=1)
    loss, acc = model.evaluate(X_test, Y_test, batch_size=32)


