import pandas as pd
import matplotlib.pyplot as plt

# Data sources
df = pd.read_csv('M11-coe_results.csv')
data = pd.read_csv('ProcessedData_.csv')

# Extracting year from 'month' and 'Registration Date'
df['Year'] = pd.to_datetime(df['month']).dt.year
data['Year'] = pd.to_datetime(data['Registration Date']).dt.year

# Filter data for the years 2010 to 2023
df_filtered = df[(df['Year'] >= 2009) & (df['Year'] <= 2024)]
data_filtered = data[(data['Year'] >= 2009) & (data['Year'] <= 2024)]

# Grouping and calculating averages
highest_quotas = df_filtered.groupby('Year')['quota'].max()
average_quotas = df_filtered.groupby('Year')['quota'].mean()
average_price_by_year = data_filtered.groupby('Year')['Price'].mean()

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 7))

# Bar plot for average car prices
ax1.bar(average_price_by_year.index, average_price_by_year, color='darkgreen', label='Average Price')

# Line plots for COE quotas
ax2 = ax1.twinx()
ax2.plot(highest_quotas.index, highest_quotas, label='Highest COE Quotas', marker='o', color='blue')
ax2.plot(average_quotas.index, average_quotas, label='Average COE Quotas', marker='o', color='orange')

# Titles and legends
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Car Price', color='darkgreen')
ax2.set_ylabel('COE Quotas', color='blue')
plt.title('Annual COE Quotas vs. Average Car Price')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Set x-axis limits to show only years 2010 to 2023
ax1.set_xlim(2010, 2023)

# Display the plot
plt.show()