import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
#load data



da = pd.read_csv('../../../Downloads/Dataset/accidents.csv')
dv = pd.read_csv('../../../Downloads/Dataset/vehicles.csv')


dc = pd.merge(da, dv, on=['accident_id'])

#print info from data
#print("accidents: \n \n \n")
#print(da.info())
#print(dv.info())


#print values from some colums

#clean dataset
dc.drop(labels = ['accident_id'], axis = 1, inplace = True)
dc.drop(labels = ['lsoa_of_accident_location'], axis = 1, inplace = True)
#location_easting_osgr, location_northing_osgr


for i in dc:
    d = []
    if i == "time":
        for j in range(0,len(dc[i])):
            h = int(dc[i][j].split(":")[0])
            m = int(dc[i][j].split(":")[1])
            d.append(h)
        dc[i] = d
    elif i == "date":
        month = []
        for j in range(0,len(dc[i])):
            y = int(dc[i][j].split("-")[0])
            m = int(dc[i][j].split("-")[1])
            day = int(dc[i][j].split("-")[2])
            month.append(m)
            d.append(dt.date(y,m,day).weekday())
        dc["Day"] = d
        dc["Month"] = month
        dc.drop(i,axis = 1, inplace=True)
    elif type(dc[i][0]) is str:
        if i == 'Sex_of_Driver' or i == 'Vehicle_Manoeuvre' or i =='Vehicle_Type' or i == 'urban_or_rural_area' or i == 'light_conditions':
            #print(dc[i].value_counts())
            try:
                indexs = dc.index[dc[i] == "-1"].tolist()
                dc.drop(indexs, axis = 0, inplace=True)
            except:
                pass

            temp_dummy = pd.get_dummies(dc[i])
            for j in temp_dummy:
                dc[i+"-"+j] = temp_dummy[j]
                #temp_dummy.rename({j: i+"-"+j}, axis=1, inplace=True)
            #dc = pd.concat([dc,temp_dummy], axis = 1)
            dc.drop(i, axis = 1,inplace=True)
        else:
            dc.drop(i, axis = 1, inplace = True) #lol same accucary (look PC)
    elif i != "Month" and i != "Day" and "weather_conditions"!=i and i!="target":
        dc.drop(i,axis=1, inplace=True)
    elif i=="weather_conditions":
        temp_dummy = pd.get_dummies(dc[i])
        for j in temp_dummy:
            if j == -1:
                continue
            dc[i+"-"+str(j)] = temp_dummy[j]
            #temp_dummy.rename({j: i+"-"+j}, axis=1, inplace=True)
            #dc = pd.concat([dc,temp_dummy], axis = 1)
        dc.drop(i, axis = 1,inplace=True)
for i in dc:
    print(dc[i].value_counts())
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
print(dc.info())
indexs = dc.index[dc["target"] == 0].tolist()
indexs = np.random.choice(indexs, int(len(indexs)/2), replace = False)
dc.drop(indexs, axis = 0, inplace=True)
print ("//////////////////////////////777777777777777777777777777777777777777777777777777777777777777777")
print(dc.info())
dc.to_csv(r'dc2.csv')
'''
#Neural Network
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical
import keras

X = dc.drop('target', axis = 1)
Y = dc.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5)
accuracies = []
losses = []
for i in range(0, 10):
    model = Sequential()
    model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(5, input_dim=10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.
    model.fit(X_train, Y_train, epochs=500, batch_size=128, verbose=1)
    loss, acc = model.evaluate(X_test, Y_test, batch_size=32)
    for j in range(0,len(X),5):
        print(model.predict(X[j:j+5]))
        print(Y[j:j+5])
'''

