# bar chart of median pricing of car from brand that has >= 100 postings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import csv file
data = pd.read_csv('ProcessedData_.csv')
# print(data)

# counts the no. of brands
brand_counts=data['Brand'].value_counts()

# counts of each brand in a column
data['Brand_Count'] = data['Brand'].transform(lambda x: brand_counts[x])

# filter out brands which are posted less than 100 times
filtered_brand= data[data['Brand_Count'] >= 100].copy()

# drop the column used for counting
filtered_brand = filtered_brand.drop(columns=['Brand_Count'])
print(brand_counts)
# print(data['Brand_Count'])
# print(filtered_brand)

# median price of each brand of car
median_prices_filtered = filtered_brand.groupby('Brand')['Price'].median().reset_index()


colours=['blue','green','orange','yellow','pink','red','purple','cyan','grey','olive']
# plotting bar graph of the median price of car brands that have at least 100 postings
fig_bar=plt.figure(figsize=(12,6))
plt.bar(median_prices_filtered['Brand'], median_prices_filtered['Price'],color=colours)
for i, price in enumerate(median_prices_filtered['Price']):
    plt.text(i,price+0.1,int(price),ha='center',va='bottom')
plt.xlabel('Brand')
plt.ylabel('Median price (SGD)')
plt.title('Median price by Brand with >= 100 listings')
# plt.xticks(rotation=45,ha='right')
plt.show()
