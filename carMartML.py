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

brand_dict={}
for i,j in zip(data['Brand'].unique().tolist(),range(1, data['Brand'].nunique())):
    brand_dict[i]=str(j)
print(brand_dict)

prices_dict={}
for i,j in zip(data['Price'].unique().tolist(),range(1, data['Price'].nunique())):
    prices_dict[i]=float(j)

depr_dict={}
for i,j in zip(data['Depreciation'].unique().tolist(),range(1, data['Depreciation'].nunique())):
    depr_dict[i]=float(j)

road_tax_dict={}
for i,j in zip(data['Road Tax'].unique().tolist(),range(1, data['Road Tax'].nunique())):
    road_tax_dict[i]=float(j)

reg_dict={}
for i,j in zip(data['Registration Date'].unique().tolist(),range(1, data['Registration Date'].nunique())):
    reg_dict[i]=str(j)

coe_left_dict={}
for i,j in zip(data['COE Left'].unique().tolist(),range(1, data['COE Left'].nunique())):
   coe_left_dict[i]=float(j)

mil_dict={}
for i,j in zip(data['Mileage'].unique().tolist(),range(1, data['Mileage'].nunique())):
    mil_dict[i]=int(j)

manufacture_dict={}
for i,j in zip(data['Manufacture Year'].unique().tolist(),range(1, data['Manufacture Year'].nunique())):
    manufacture_dict[i]=str(j)

trans_dict={}
for i,j in zip(data['Transmission'].unique().tolist(),range(1, data['Transmission'].nunique())):
    trans_dict[i]=str(j)

dereg_dict={}
for i,j in zip(data['Deregistration'].unique().tolist(),range(1, data['Deregistration'].nunique())):
    dereg_dict[i]=int(j)

omv_dict={}
for i,j in zip(data['OMV'].unique().tolist(),range(1, data['OMV'].nunique())):
    omv_dict[i]=int(j)

arf_dict={}
for i,j in zip(data['ARF'].unique().tolist(),range(1, data['ARF'].nunique())):
    arf_dict[i]=int(j)

coe_price_dict={}
for i,j in zip(data['COE Price'].unique().tolist(),range(1, data['COE Price'].nunique())):
    coe_price_dict[i]=float(j)

eng_dict={}
for i,j in zip(data['Engine Capacity'].unique().tolist(),range(1, data['Engine Capacity'].nunique())):
    eng_dict[i]=int(j)

power_dict={}
for i,j in zip(data['Power'].unique().tolist(),range(1, data['Power'].nunique())):
    power_dict[i]=float(j)

no_owners_dict={}
for i,j in zip(data['No. Of Owners'].unique().tolist(),range(1, data['No. Of Owners'].nunique())):
    no_owners_dict[i]=int(j)

vehicle_type_dict={}
for i,j in zip(data['Vehicle Type'].unique().tolist(),range(1, data['Vehicle Type'].nunique())):
    vehicle_type_dict[i]=str(j)

#training model & testing samples
train_x,test_x,train_y,test_y=train_test_split(data.drop('Price',axis=1),data['Price'],test_size=0.2,random_state=89)

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
with open("brand_dictionary.json",'w') as f:
    json.dump(brand_dict,f)
f.close()
with open("prices_dictionary.json",'w')as f:
    json.dump(prices_dict,f)
f.close()
with open("depreciation_dictionary.json",'w') as f:
    json.dump(depr_dict,f)
f.close()
with open("road_tax_dictionary.json",'w') as f:
    json.dump(road_tax_dict,f)
f.close()
with open("registration_dictionary.json",'w')as f:
    json.dump(reg_dict,f)
f.close()
with open("coe_left_dictionary.json",'w') as f:
    json.dump(coe_left_dict,f)
f.close()
with open("mileage_dictionary.json",'w') as f:
    json.dump(mil_dict,f)
f.close()
with open("manufacture_dictionary.json",'w') as f:
    json.dump(manufacture_dict,f)
f.close()
with open("transmission_dictionary.json",'w') as f:
    json.dump(trans_dict,f)
f.close()
with open("dereg_dictionary.json",'w') as f:
    json.dump(dereg_dict,f)
f.close()
with open("omv_dictionary.json",'w') as f:
    json.dump(omv_dict,f)
f.close()
with open("arf_dictionary.json",'w') as f:
    json.dump(arf_dict,f)
f.close()
with open("coe_price_dictionary.json",'w') as f:
    json.dump(coe_price_dict,f)
f.close()
with open("engine_dictionary.json",'w')as f:
    json.dump(eng_dict,f)
f.close()
with open("power_dictionary.json",'w')as f:
    json.dump(power_dict,f)
f.close()
with open("no_owners_dictionary.json",'w')as f:
    json.dump(no_owners_dict,f)
f.close()
with open("vehicle_type_dictionary.json",'w')as f:
    json.dump(vehicle_type_dict,f)
f.close()
