import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Data sources
df = pd.read_csv('M11-coe_results.csv')

# Extracting year from 'month' and 'Registration Date'
df['Year'] = pd.to_datetime(df['month']).dt.year

# Grouping and calculating averages
highest_quotas = df.groupby('Year')['quota'].max()
average_quotas = df.groupby('Year')['quota'].mean()

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 7))

# Bar plot for average car prices
bar_plot = ax1.bar(highest_quotas.index, highest_quotas, color='darkgreen', label='Yearly Quota')

# Line plots for COE quotas
ax2 = ax1.twinx()
line1, = ax2.plot(highest_quotas.index, highest_quotas, label='Highest Price', marker='o', color='blue')
line2, = ax2.plot(average_quotas.index, average_quotas, label='Average Price', marker='o', color='orange')

# Titles and legends
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Car Price', color='darkgreen')
ax2.set_ylabel('COE Quotas', color='blue')
plt.title('Annual COE Quotas vs Premium Price')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')


# Add interactive annotations
annotations = mplcursors.cursor([bar_plot, line1, line2], hover=True)

@annotations.connect("add")
def on_add(sel):
    year = int(sel.target[0])
    yearly_quota = highest_quotas[year]
    highest_price = highest_quotas[year]  # Assuming highest_quota is equivalent to highest_price
    average_price = average_quotas[year]

    sel.annotation.set_text(
        f'Year: {year}\nYearly Quota: {yearly_quota}\nHighest Price: ${highest_price}\nAverage Price: ${average_price:.2f}'
        # Format to 2 decimal places
    )
# Display the plot
plt.show()