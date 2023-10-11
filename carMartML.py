import json
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

# read the cleaned data
data = pd.read_csv("ProcessedData.csv")

#drop car brand names
data_rm_brand = data.drop('Brand', axis=1)

#change car Registration Dates str type to datetime type
data_rm_brand['Registration Date'] = pd.to_datetime(data['Registration Date'])
data_rm_brand['Registration Date'].dtypes

#encode Transmission (Auto='1', Manual='0')
#Define a mapping dictionary
mapping_dict = {'Auto': 1, 'Manual': 0}

# Apply the mapping to the "Transmission" column
data_rm_brand['Transmission'] = data_rm_brand['Transmission'].map(mapping_dict)

#Rename the column to 'Transmission' to reflect encoding
data_rm_brand.rename(columns={'Transmission': 'Transmission'}, inplace=True)

#encode car types
# Define a mapping dictionary
mapping_dict2 = {'Hatchback': 0,'Mid-Sized Sedan': 1, 'MPV': 2, 'Luxury Sedan': 3, 'SUV': 4, 'Sports Car': 5}

# Apply the mapping to the "Vehicle Type" column
data_rm_brand['Vehicle Type'] = data_rm_brand['Vehicle Type'].map(mapping_dict2)

#Rename 'Vehicle Type' to reflect encoding
data_rm_brand.rename(columns={'Vehicle Type': 'Vehicle Type'}, inplace=True)

#training model & testing samples
train_x,test_x,train_y,test_y=train_test_split(data.drop('Price',axis=1),data['Price'],test_size=0.2,random_state=89)

#XGBRegressor
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
