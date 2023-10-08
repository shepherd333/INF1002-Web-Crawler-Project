import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
df = pd.read_csv(r"C:\Users\tohzh\PycharmProjects\INF1002-Web-Crawler-Project\newUsedCars_20sep.csv")

#print(df.shape) # (rows, columns)
#print(df.head(10)) # top 10 rows

#box plot of price vs mileage
depreciation_by_vehicle_type = df[['Depreciation', 'Vehicle Type']]
sns.boxplot(x='Vehicle Type', y='Depreciation', data=depreciation_by_vehicle_type)
plt.xlabel('Vehicle Type')
plt.ylabel('Depreciation')
plt.title('Box Plot of Depreciation by Vehicle Type')
plt.xticks(rotation=45)
plt.show()

'''
plt.hist('Prices', bins=20, edgecolor='black')
plt.xlabel('Prices')
plt.ylabel('Frequency')
plt.title('Histogram of Prices')
plt.show()
'''











