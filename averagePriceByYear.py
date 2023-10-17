import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import numpy as np

# data source
data = pd.read_csv('ProcessedData_.csv')


#data['Year'] = pd.to_datetime(data['Registration Date'])
# Group by registration date and calculate mean price
price_by_date = data.groupby('Registration Date')['Price'].mean().reset_index()

# Convert the 'Registration Date' column to Pandas DateTime format and extract the year
data['Year'] = pd.to_datetime(data['Registration Date']).dt.year

# Group by year and calculate the mean price
average_price_by_year = data.groupby("Year")["Price"].median()

# Plotting the average price by year
average_price_by_year.sort_index().plot(kind='bar', color='darkgreen', figsize=(10, 7),
                                        title="Median Price of a Car by Year")
plt.xlabel('Year')
plt.ylabel('Price')
plt.show()
# Plot price trends over time
#plt.figure(figsize=(12, 6))
#plt.plot(price_by_date['Registration Date'], price_by_date['Price'])
#plt.hist(prices_data, bins=20, edgecolor='black')
#data.groupby("Year")["Price"].mean().sort_values().plot(kind='bar', color='darkgreen',figsize=(10,7),title="Average Price of a Car\by Year");

#plt.xlabel('Price')
#plt.ylabel('Registration Year')
#plt.title('Average Price of Car by Registration Year')
#plt.show()












"""
data['Prices'] = data['Prices'].str.replace(',', '').astype(float)
prices_data = data['Prices']

# Calculate the number of bins needed to represent 10,000 intervals
num_bins = int((max(prices_data) - min(prices_data)) / 10000) + 1

# Create the histogram with adjusted bins and x-axis labels
plt.hist(prices_data, bins=np.arange(min(prices_data), max(prices_data) + 10000, 10000), edgecolor='black')

# Set custom x-axis labels representing 10,000 intervals
plt.xticks(np.arange(min(prices_data), max(prices_data) + 10000, 10000),
           ['${:,}'.format(i) for i in np.arange(min(prices_data), max(prices_data) + 10000, 10000)])

plt.xlabel('Prices')
plt.ylabel('Frequency')
plt.title('Histogram of Prices')
plt.show()
"""

"""
data['Reg Date'] = pd.to_datetime(data['Reg Date'])
# Group by registration date and calculate mean price
price_by_date = data.groupby('Reg Date')['Prices'].mean().reset_index()

# Plot price trends over time
plt.figure(figsize=(12, 6))
plt.plot(price_by_date['Reg Date'], price_by_date['Prices'])
plt.xlabel('Registration Date')
plt.ylabel('Mean Price')
plt.title('Price Trends Over Time')
plt.show()
"""













