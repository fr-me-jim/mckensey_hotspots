import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
#load data
da = pd.read_csv('./Dataset/accidents.csv')


#print info from data
#print("accidents: \n \n \n")
#print(da.info())


#print values from some colums
#print(da.target.value_counts())


#clean dataset
da.drop(labels = ['lsoa_of_accident_location'], axis = 1, inplace = True)


for i in da:
    d = []
    if i == "time":
        for j in range(0,len(da[i])):
            #print(j)
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
        try:
            if da[i].value_counts()["-1"] < len(da[i]) * .05:
                #delete -1
                indexs = da.index[da[i] == "-1"].tolist()
                da.drop(indexs, axis = 0, inplace=True)
                print("Ok: " + i)
            else:
                #problematic colums
                print("Ko: " + i)
        except:
            print("No -1: "+ i)

        pass    
    #print(i+" "+str(type(da[i][0])))
road1_class = pd.get_dummies(da['1st_road_class'])
road2_class = pd.get_dummies(da['2nd_road_class'])
junc_detail = pd.get_dummies(da['junction_detail'])
ped_con = pd.get_dummies(da['pedestrian_crossing-human_control'])
ped_fac = pd.get_dummies(da['pedestrian_crossing-physical_facilities'])
light = pd.get_dummies(da['light_conditions'])
road_cond = pd.get_dummies(da['road_surface_conditions'])
special_cond = pd.get_dummies(da['carriageway_hazards'])
u_r = pd.get_dummies(da['urban_or_rural_area'])

police_force = pd.get_dummies(da['police_force'])
local_aut_district = pd.get_dummies(da['local_authority_district'])
local_aut_high = pd.get_dummies(da['local_authority_highway'])


#date/time---------------------------------------------------

"""
from sklearn.decomposition import PCA

pca = PCA()
da_pca = pca.fit_transform(da)
y_variance = pca.explained_variance_ratio_
pd.DataFrame(pca.components_, columns=df.columns)


sns.barplot(x=[i for i in range(len(y_variance))], y=y_variance)
plt.title("PCA")
"""
