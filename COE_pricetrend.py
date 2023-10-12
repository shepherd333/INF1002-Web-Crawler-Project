import pandas as pd
import matplotlib.pyplot as plt

# Read the data and preprocess it
df = pd.read_csv('M11-coe_results.csv')
df = df.drop(columns=['bids_success', 'bids_received', 'quota'])
df = df.drop(df[df['vehicle_class'].isin(['Category C', 'Category D', 'Category E'])].index)
df['month'] = pd.to_datetime(df['month'])
df['month'] = df.apply(lambda row: row['month'].replace(day=1) if row['bidding_no'] == 1 else row['month'].replace(day=15), axis=1)

# Calculate the 7-day rolling average for each category
df['rolling_avg'] = df.groupby(['vehicle_class'])['premium'].transform(lambda x: x.rolling(7, min_periods=1).mean())

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for Category A with blue color and hatch pattern, set alpha for transparency
ax1.bar(df[df['vehicle_class'] == 'Category A']['month'], df[df['vehicle_class'] == 'Category A']['premium'], width=10, label='Category A Premium', color='blue', alpha=1, hatch='////')

# Bar chart for Category B with red color and a different hatch pattern, set alpha for transparency
ax1.bar(df[df['vehicle_class'] == 'Category B']['month'], df[df['vehicle_class'] == 'Category B']['premium'], width=10, label='Category B Premium', color='red', alpha=0.5, hatch='\\\\\\\\')

# Set the primary y-axis (left)
ax1.set_xlabel('Month')
ax1.set_ylabel('COE Premium')
ax1.set_title('COE Premium and 7-Period Rolling Average')

# Create a line chart for the rolling averages
ax2 = ax1.twinx()
ax2.plot(df[df['vehicle_class'] == 'Category A']['month'], df[df['vehicle_class'] == 'Category A']['rolling_avg'], label='Category A Rolling Avg', color='r')
ax2.plot(df[df['vehicle_class'] == 'Category B']['month'], df[df['vehicle_class'] == 'Category B']['rolling_avg'], label='Category B Rolling Avg', color='y')

# Set the secondary y-axis (right)
ax2.set_ylabel('Rolling Average')

# Combine the legends
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right')

plt.show()
