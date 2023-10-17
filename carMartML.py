import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import xgboost as xgb
import pickle
import tkinter as tk
from datetime import datetime

# read the cleaned data
data = pd.read_csv("ProcessedData_.csv")

#drop car brand names
data_rm_brand = data.drop(['Listing ID','Brand', 'Listing URL'], axis=1)

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
mapping_dict2 = {'Hatchback': 1,'Mid-Sized Sedan': 2, 'MPV': 3, 'Luxury Sedan': 4, 'SUV': 5, 'Sports Car': 6, 'Stationwagon': 7}
# Apply the mapping to the "Vehicle Type" column
data_rm_brand['Vehicle Type'] = data_rm_brand['Vehicle Type'].map(mapping_dict2)
#Rename 'Vehicle Type' to reflect encoding
data_rm_brand.rename(columns={'Vehicle Type': 'Vehicle Type'}, inplace=True)
#data_rm_brand.head()

#Covert registration date format to encode
registration_date_datetime = pd.to_datetime(data_rm_brand['Registration Date'], format='%y-%m-%d')
#Encode the registration date to an integer.
encoded_registration_date = registration_date_datetime.dt.year * 10000 + registration_date_datetime.dt.month * 100 + registration_date_datetime.dt.day
#print(encoded_registration_date)
encoded_registration_date = encoded_registration_date.astype(int)

#start of Data Visualization

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
#drop high-corelation variables
data_rm_brand.drop(['Depreciation','Registration Date','Manufacture Year','ARF','Engine Capacity','Power'],axis=1,inplace=True)
remaining_columns = data_rm_brand.columns
#save into csv file
data_rm_brand.to_csv('remaining_columns.csv', index=False, columns=remaining_columns)

#Our chosen dropped high-corelation variables assessed by ML model
# Assuming X is your feature data and y is your target variable
data_rm_brand = pd.read_csv('remaining_columns.csv')
# Split the data into input features (X) and target variable (y)
X = data_rm_brand
y = data_rm_brand['Price']
# RFE for XGBoost
xgb_model = XGBRegressor()
rfe_xgb = RFE(estimator=xgb_model, n_features_to_select=10)  # Adjust the number of features to select as needed
rfe_xgb.fit(X, y)
selected_features_xgb = X.columns[rfe_xgb.support_]
# RFE for Linear Regression
lr_model = LinearRegression()
rfe_lr = RFE(estimator=lr_model, n_features_to_select=10)  # Adjust the number of features to select as needed
rfe_lr.fit(X, y)
selected_features_lr = X.columns[rfe_lr.support_]
# RFE for RandomForest
rf_model = RandomForestRegressor()
rfe_rf = RFE(estimator=rf_model, n_features_to_select=10)  # Adjust the number of features to select as needed
rfe_rf.fit(X, y)
selected_features_rf = X.columns[rfe_rf.support_]
# Combine selected features from all models (intersection)
selected_features = list(set(selected_features_xgb) & set(selected_features_lr) & set(selected_features_rf))
# Create a new dataset with selected features by ML model
selected_X = X[selected_features]
selected_X.to_csv('MLselected_columns.csv', index=False, columns=selected_X)

# Re-visualizing the correlation matrix with ML selected variables
#sns.set(style="white")
# Creating the data
#data = selected_X.corr()
# Generate a mask for the upper triangle
#mask = np.zeros_like(data, dtype=np.bool_)
#mask[np.triu_indices_from(mask)] = True
# Set up the matplotlib figure to control size of heatmap
#fig, ax = plt.subplots(figsize=(15,15))
# Create a custom color palette
#cmap = \
#sns.diverging_palette(133, 10, as_cmap=True)  # as_cmap returns a matplotlib colormap object rather than a list of colors
# Green = Good (low correlation), Red = Bad (high correlation) between the independent variables
# Plot the heatmap
#sns.heatmap(data, mask=mask, annot=True, square=True, cmap=cmap , vmin=-1, vmax=1,ax=ax);
# Prevent Heatmap Cut-Off Issue
#bottom, top = ax.get_ylim()
#ax.set_ylim(bottom + 0.5, top - 0.5)
# ML selected variables
#sns.pairplot(selected_X);

#Histograms plot with ML selected variables
#fig, ax = plt.subplots(figsize=(15,15))
#pd.DataFrame.hist(selected_X,ax=ax)

#chosen 5 of the ML selected variables for logging (OMV,Curb Weight, Road Tax, COE Price and Deregisteration)
data_rm_brand_only_OMV_logged = data_rm_brand.copy().drop(columns=['Transmission','Deregistration','Vehicle Type'], axis=1)
data_rm_brand_only_OMV_logged['OMV'] = np.log(data_rm_brand_only_OMV_logged['OMV'])
data_rm_brand_only_OMV_logged.head()
data_rm_brand_only_OMV_logged.to_csv('OMV_columns.csv', index=False)

data_rm_brand_only_curbweight_logged = data_rm_brand.copy().drop(columns=['Transmission','Deregistration','Vehicle Type'], axis=1)
data_rm_brand_only_curbweight_logged['Curb Weight'] = np.log(data_rm_brand_only_curbweight_logged['Curb Weight'])
data_rm_brand_only_curbweight_logged.head()
data_rm_brand_only_curbweight_logged.to_csv('Curb_Weight_columns.csv', index=False)

data_rm_brand_only_roadtax_logged = data_rm_brand.copy().drop(columns=['Transmission','Deregistration','Vehicle Type'], axis=1)
data_rm_brand_only_roadtax_logged['Road Tax'] = np.log(data_rm_brand_only_roadtax_logged['Road Tax'])
data_rm_brand_only_roadtax_logged.head()
data_rm_brand_only_roadtax_logged.to_csv('Road_Tax_columns.csv', index=False)

data_rm_brand_only_COE_logged = data_rm_brand.copy().drop(columns=['Transmission','Deregistration','Vehicle Type'], axis=1)
data_rm_brand_only_COE_logged['COE Price'] = np.log(data_rm_brand_only_COE_logged['COE Price'])
data_rm_brand_only_COE_logged.head()
data_rm_brand_only_COE_logged.to_csv('COE_Price_columns.csv', index=False)

data_rm_brand_only_owners_logged = data_rm_brand.copy().drop(columns=['Transmission','Deregistration','Vehicle Type'], axis=1)
data_rm_brand_only_owners_logged['No. Of Owners'] = np.log(data_rm_brand_only_owners_logged['No. Of Owners'])
data_rm_brand_only_owners_logged.head()
data_rm_brand_only_owners_logged.to_csv('No_Of_Owners_columns.csv', index=False)

# Before and After logging Histogram comparisons
# Logged Histogram
#data_rm_brand_only_OMV_logged = pd.read_csv('OMV_columns.csv')
#data_rm_brand_only_curbweight_logged = pd.read_csv('Curb_Weight_columns.csv')
#data_rm_brand_only_roadtax_logged = pd.read_csv('Road_Tax_columns.csv')
#data_rm_brand_only_COE_logged = pd.read_csv('COE_Price_columns.csv')
#data_rm_brand_only_deregistration_logged = pd.read_csv('Deregistration_columns.csv')
# **Log-transform the data**
#logged_data = {}
#for column in ['OMV', 'Curb Weight', 'Road Tax', 'COE Price', 'Deregistration']:
#    logged_data[column] = np.log(data_rm_brand_only_OMV_logged[column])
# Create a figure and axes object
#fig, axs = plt.subplots(5, 2, figsize=(15,15))
# Plot the histograms 
#axs[0, 0].hist(data_rm_brand_only_OMV_logged['OMV'], label='OMV (Original)')
#axs[0, 1].hist(logged_data['OMV'], label='OMV (Logged)')
#axs[1, 0].hist(data_rm_brand_only_curbweight_logged['Curb Weight'], label='Curb Weight (Original)')
#axs[1, 1].hist(logged_data['Curb Weight'], label='Curb Weight (Logged)')
#axs[2, 0].hist(data_rm_brand_only_roadtax_logged['Road Tax'], label='Road Tax (Original)')
#axs[2, 1].hist(logged_data['Road Tax'], label='Road Tax (Logged)')
#axs[3, 0].hist(data_rm_brand_only_COE_logged['COE Price'], label='COE Price (Original)')
#axs[3, 1].hist(logged_data['COE Price'], label='COE Price (Logged)')
#axs[4, 0].hist(data_rm_brand_only_deregisteration_logged['Deregistration'], label='Deregistration (Original)')
#axs[4, 1].hist(logged_data['Deregistration'], label='Deregistration (Logged)')
# Add titles and labels
#plt.suptitle('Distribution of Vehicle Features (Original vs. Logged)')
#for ax in axs.ravel():
#    ax.set_xlabel(ax.get_title())
#    ax.set_ylabel('Count')
#    ax.legend()
# Show the plot
#plt.show()

# end of Data Visualization

# merge loggings for training datasets
# Read the five CSV files into Pandas DataFrames
df1 = pd.read_csv('OMV_columns.csv')
df2 = pd.read_csv('Curb_Weight_columns.csv')
df3 = pd.read_csv('Road_Tax_columns.csv')
df4 = pd.read_csv('COE_Price_columns.csv')
df5 = pd.read_csv('No_Of_Owners_columns.csv')

#df = pd.concat([df1, df2], ignore_index=True)
# Save the merged DataFrame to a new CSV file
#df.to_csv('merged_logging.csv', index=False)
#df = pd.concat([df1, df2, df3], ignore_index=True)
# Save the merged DataFrame to a new CSV file
#df.to_csv('merged_logging2.csv', index=False)
#df = pd.concat([df1, df2, df3, df4], ignore_index=True)
# Save the merged DataFrame to a new CSV file
#df.to_csv('merged_logging3.csv', index=False)

# Merge the five DataFrames into a single DataFrame
df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# Save the merged DataFrame to a new CSV file
df.to_csv('merged_logging4.csv', index=False)

#Use the final merged logging file to decide which training model to use based on the r2 scores
# LinearRegression R2 scores
# 0.44667675264383067
# XGBRegressor R2 scores
# 0.9665030424772889
# RandomForrest R2 scores
# 0.9623617067325756
#Cross-Validation of R2 scores
#XGBRegressor Cross-Validation R2 scores: [0.04788376 0.74292074 0.84416435 0.78959246 0.95804782]
#XGBRegressor Mean R2: 0.676521826739158
#XGBRegressor Standard Deviation of R2: 0.32240983328864037

# ML model training
# Read the CSV file into a Pandas DataFrame
data = pd.read_csv("merged_logging4.csv")
# Split the data into training and testing sets
train_x, test_x, train_y, test_y = train_test_split(data.drop('Price', axis=1), data['Price'], test_size=0.25, random_state=42)
# Create an XGBoost regressor
xgr = xgb.XGBRegressor(n_estimators=1000, learning_rate=0.1, max_depth=5)
# Train the model on the training data
xgr.fit(train_x, train_y)
# Make predictions on the test data
predict = xgr.predict(test_x)
# Evaluate the performance of the model
#print('MAE', mean_absolute_error(predict, test_y))
#print('R2', r2_score(predict, test_y))

# from ProcessedData.csv (old)
# MAE 4373.667899687914
# R2 0.9871182583379438

#from ProcessedData_.csv (updated)
#MAE 8240.562093914996
#R2 0.9313314594769386

# Save the model to a file
with open('model.pkl', 'wb') as f:
       pickle.dump(xgr, f)
