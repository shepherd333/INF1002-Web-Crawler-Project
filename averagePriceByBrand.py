import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import numpy as np

# data source
data = pd.read_csv('ProcessedData_.csv')

# Plotting the average price by year
data.groupby("Brand")["Price"].median().sort_values().plot(kind='bar',color='darkgreen',figsize=(10,7),title="Median Car Price per Brand");
plt.xlabel('Brands')
plt.ylabel('Median Price')
plt.show()