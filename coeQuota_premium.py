import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Data sources
df = pd.read_csv('M11-coe_results.csv')

# Extracting year from 'month' and 'Registration Date'
df['Year'] = pd.to_datetime(df['month']).dt.year

# Filter data for Vehicle Class A and B
filtered_df = df[df['vehicle_class'].isin(['Category A', 'Category B'])]

# Grouping and calculating averages for the filtered data
highest_premium = filtered_df.groupby('Year')['premium'].max()
average_premium = filtered_df.groupby('Year')['premium'].mean()
yearly_quota = filtered_df.groupby('Year')['quota'].max()

print(highest_premium)
print(average_premium)
'''
quota_to_price_scaling_factor = 1000
highest_prices = highest_quotas * quota_to_price_scaling_factor
average_prices = average_quotas * quota_to_price_scaling_factor
'''
# Plotting
fig, ax1 = plt.subplots(figsize=(10, 7))

# Bar plot for average car prices
#bar_plot = ax1.bar(highest_prices.index, highest_prices, color='skyblue', label='Yearly Quota')
bar_plot = ax1.bar(yearly_quota.index, yearly_quota, color='skyblue', label='Yearly Quota')

# Line plots for COE quotas
ax2 = ax1.twinx()
line1, = ax2.plot(highest_premium.index, highest_premium, label='Highest Price', marker='o', color='blue')
line2, = ax2.plot(average_premium.index, average_premium, label='Average Price', marker='o', color='orange')

# Titles and legends
ax1.set_xlabel('Year')
ax1.set_ylabel('Yearly Quota', color='skyblue')
ax2.set_ylabel('Premium Price', color='blue')
plt.title('Annual COE Quotas vs Premium Price')
ax1.legend(loc='lower left')
ax2.legend(loc='lower right')


# Add interactive annotations
annotations = mplcursors.cursor([bar_plot, line1, line2], hover=True)

@annotations.connect("add")
def on_add(sel):
    year = int(sel.target[0])
    yearly_quotas = yearly_quota[year]
    highest_price = highest_premium[year]  # Assuming highest_quota is equivalent to highest_price
    average_price = average_premium[year]

    sel.annotation.set_text(
        f'Year: {year}\nYearly Quota: {yearly_quotas}\nHighest Premium: ${highest_price:,.2f}\nAverage Premium: ${average_price:,.2f}'
    )
# Display the plot
plt.show()