import pandas as pd
import numpy as np
from datetime import datetime
import csv

# reading original csv
data=pd.read_csv('UsedCars_7oct.csv')
# print(data.info())

# remove rows with N.A. or -
data=data[~data.isin(['N.A.', '-', 'N.A']).any(axis=1)]
# print(data)

# change remove comma in prices
data['Prices']=data['Prices'].str.replace(',','')
data['Prices']=data['Prices'].astype(float)

# change depreciation to float and get rid of /yr
remove=['$',',','/','y','r']
data['Depreciation']=data['Depreciation'].apply(lambda x: ''.join([i for i in x if i not in remove]))
data['Depreciation']=data['Depreciation'].astype(float)

# reg date to date
data['Reg Date']=pd.to_datetime(data['Reg Date'],format='%d-%b-%Y', errors='coerce')

# engine cap to int
remove_eng=[',','c']
data['Eng Cap']=data['Eng Cap'].apply(lambda x: ''.join([e for e in x if e not in remove_eng]))
data['Eng Cap']=data['Eng Cap'].astype(int)

# mileage to int
remove_mile=[',','k','m']
data['Mileage']=data['Mileage'].apply(lambda x: ''.join([m for m in x if m not in remove_mile]))
data['Mileage']=data['Mileage'].astype(int)

# write to new csv file
data.to_csv('cleaned_7oct.csv', index=False, encoding='utf-8')
