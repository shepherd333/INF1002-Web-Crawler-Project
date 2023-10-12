# Average COE prices for each category from 2010 - Oct 2023
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# importing data set
data=pd.read_csv('coe_cars.csv')

# counting the number of each cat
cat_count=data['vehicle_class'].value_counts()
print(cat_count)

# convert month to datetime format
data['month']=pd.to_datetime(data['month'],format='%Y-%m')

# take only the year
data['Year']=data['month'].dt.year

# get average premium for each class per year
avg_premium=data.groupby(['Year','vehicle_class'])['premium'].mean().reset_index()

# round the ave premium to whole number
round_avg_premium=round(avg_premium)
print(round_avg_premium)

# reshaping data using pivot function to help with graph
pivot_table=avg_premium.pivot(index='Year', columns='vehicle_class',values='premium')

#  graphing
pivot_table.plot(kind='line',marker='.',figsize=(10,6))
plt.xlabel('Year')
plt.ylabel('Average Premium (SGD)')
plt.title('Average COE prices for each category from 2010 - Oct 2023')

plt.legend(title='Vehicle Class')
plt.grid(True)
plt.show()