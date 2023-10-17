import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('ProcessedData_.csv')

# Convert 'RegistrationDate' to a datetime format
df['Registration Date'] = pd.to_datetime(df['Registration Date'])

# Extract year and month from the 'RegistrationDate'
df['Year'] = df['Registration Date'].dt.year
df = df[df['Year'] >= 2010]
# Group by year and month and count the number of registrations
registration_counts = df.groupby(['Year']).size().reset_index(name='Count')

# Display the resulting DataFrame
print(registration_counts)

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(registration_counts['Year'], registration_counts['Count'], marker='o')

# Customize the plot
plt.xlabel('Year')
plt.ylabel('Number of Registrations')
plt.title('Number of Vehicles Registered by Year')
plt.grid(True)
plt.show()





