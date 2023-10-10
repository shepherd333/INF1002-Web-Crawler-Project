import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest,f_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import pickle
from datetime import datetime

## Extracting name of files from directory
#files=[i for i in os.listdir() if 'csv' in i and 'unclean' not in i]
#print(files)
## Creating dataframe by reading and appending csv
#cars=pd.concat([pd.read_csv(i) for i in files],ignore_index=True)
#cars.head()

# read the cleaned data
data = pd.read_csv("ProcessedData.csv")

#columns for training data model
#Model = str
#Prices = float
#Depreciation = float
#Registration Date = date
#Engine Capacity = int(cc)
#Mileage = int(km)
#Vehicle Type = str

model_dict={}
for i,j in zip(cars['model'].unique().tolist(),range(cars['model'].nunique())):
    model_dict[i]=str(j)

prices_dict={}
for i,j in zip(cars['prices'].unique().tolist(),range(cars['prices'].nunique())):
    prices_dict[i]=float(j)

depr_dict={}
for i,j in zip(cars['depreciation'].unique().tolist(),range(cars['depreciation'].nunique())):
    depr_dict[i]=float(j)

reg_dict={}
for i,j in zip(cars['registration'].unique().tolist(),range(cars['registration'].nunique())):
    reg_dict[i]=datetime(j)

engine_dict={}
for i,j in zip(cars['engine'].unique().tolist(),range(cars['engine'].nunique())):
    engine_dict[i]=int(j)

dist_dict={}
for i,j in zip(cars['mileage'].unique().tolist(),range(cars['mileage'].nunique())):
    dist_dict[i]=int(j)

category_dict={}
for i,j in zip(cars['type'].unique().tolist(),range(cars['type'].nunique())):
    category_dict[i]=str(j)

#training model & testing samples
train_x,test_x,train_y,test_y=train_test_split(cars.drop('price',axis=1),cars['price'],test_size=0.2,random_state=89)

#choose the better out of the 2 ensemble algorithm for prediction regression-based task output
#1. randomforestregressor 
rfr=RandomForestRegressor(n_estimators=1000,max_depth=15)
rfr.fit(train_x,train_y)
predict=rfr.predict(test_x)
print('MAE',mean_absolute_error(predict,test_y))
print('R2',r2_score(predict,test_y))
#expected example output (higher the score the better the accuracy)
#MAE 1425.9924792171153
#R2 0.9282483356510569

#2. XGBRegressor 
xgr=XGBRegressor(n_estimators=1000,learning_rate=0.1,max_depth=5)
xgr.fit(train_x,train_y)
predict=xgr.predict(test_x)
print('MAE',mean_absolute_error(predict,test_y))
print('R2',r2_score(predict,test_y))
#expected example output (higher the score the better the accuracy)
#MAE 1322.161939034648
#R2 0.9394056654633186

#save the model
filename = 'trainedcarML.sav'
pickle.dump(xgr, open(filename, 'wb'))
with open("model_dictionary.json",'w') as f:
    json.dump(model_dict,f)
f.close()
with open("prices_dictionary.json",'w')as f:
    json.dump(prices_dict,f)
f.close()
with open("depreciation_dictionary.json",'w') as f:
    json.dump(depr_dict,f)
f.close()
with open("registration_dictionary.json",'w')as f:
    json.dump(reg_dict,f)
f.close()
with open("engine_dictionary.json",'w')as f:
    json.dump(engine_dict,f)
with open("mileage_dictionary.json",'w')as f:
    json.dump(dist_dict,f)
with open("category_dictionary.json",'w')as f:
    json.dump(category_dict,f)
f.close()
