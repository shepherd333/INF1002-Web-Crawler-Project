import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import numpy as np

#HISTOGRAM

data = pd.read_csv(r"C:\Users\tohzh\PycharmProjects\INF1002-Web-Crawler-Project\newUsedCars_20sep.csv")

data['Prices'] = data['Prices'].str.replace(',', '').astype(int)
prices_data = data['Prices']
plt.hist(prices_data, bins=20, edgecolor='black')

plt.xlabel('Prices')
plt.ylabel('Frequency')
plt.title('Histogram of Prices')
plt.show()

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













