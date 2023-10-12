import pandas as pd
import numpy as np
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

#Covert registration date format to encode
registration_date_datetime = pd.to_datetime(data_rm_brand['Registration Date'], format='%y-%m-%d')
#Encode the registration date to an integer.
encoded_registration_date = registration_date_datetime.dt.year * 10000 + registration_date_datetime.dt.month * 100 + registration_date_datetime.dt.day


#Corr Matrix
#data_rm_brand.corr()
#How each feature relates to price
#data_rm_brand.corr()['Price'].sort_values(ascending=False)
#Corr Matrix Heatmap Visualization
#sns.set(style="white")
#Generate a mask for the upper triangle
#mask = np.zeros_like(data_rm_brand.corr(), dtype=np.bool_)
#mask[np.triu_indices_from(mask)] = True
#Set up the matplotlib figure to control size of heatmap
#fig, ax = plt.subplots(figsize=(15,15))
#Create a custom color palette
#cmap = \
#sns.diverging_palette(133, 10, as_cmap=True)  # as_cmap returns a matplotlib colormap object rather than a list of colors
#Green = Good (low correlation), Red = Bad (high correlation) between the independent variables
#Plot the heatmap
#sns.heatmap(data_rm_brand.corr(), mask=mask, annot=True, square=True, cmap=cmap , vmin=-1, vmax=1,ax=ax);
# Prevent Heatmap Cut-Off Issue
#bottom, top = ax.get_ylim()
#ax.set_ylim(bottom + 0.5, top - 0.5)

#Corr Matrix v2.0
sns.set(style="white")
# Creating the data
data = data_rm_brand.corr()
#Generate a mask for the upper triangle
mask = np.zeros_like(data, dtype=np.bool_)
mask[np.triu_indices_from(mask)] = True
#Set up the matplotlib figure to control size of heatmap
fig, ax = plt.subplots(figsize=(15,15))
#Create a custom color palette
cmap = \
sns.diverging_palette(133, 10, as_cmap=True)  # as_cmap returns a matplotlib colormap object rather than a list of colors
#Green = Good (low correlation), Red = Bad (high correlation) between the independent variables
#Plot the heatmap
sns.heatmap(data, mask=mask, annot=True, square=True, cmap=cmap , vmin=-1, vmax=1,ax=ax);
#Prevent Heatmap Cut-Off Issue
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)

#Performing a pairplot to visualize the data trends of the variables
#Show corelation between 2 variables (eg Price VS Depreciation --> negative relationship? Why?)
sns.pairplot(data_rm_brand);

# Slicing Data into Independent Variables (Features='features') and Dependent Variable (Target'y')
features = data_rm_brand[['Price', 'Depreciation', 'Road Tax', 'Registration Date', 'COE Left',
       'Mileage', 'Manufacture Year', 'Transmission', 'Deregistration', 'OMV',
       'ARF', 'COE Price', 'Engine Capacity', 'Power', 'Curb Weight',
       'No. Of Owners', 'Vehicle Type']].astype('category')
y= data_rm_brand['Price'].astype(float)

#Histograph of all Variables (Columns) in DataFrame
fig, ax = plt.subplots(figsize=(15,15))
pd.DataFrame.hist(data_rm_brand,ax=ax)

#BREAKPOINT HERE (until ready to test training)
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
