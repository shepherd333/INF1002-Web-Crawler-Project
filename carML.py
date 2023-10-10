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
