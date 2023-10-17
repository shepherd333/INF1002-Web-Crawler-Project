import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import tkinter as tk
from tkinter import simpledialog, messagebox

# Data source (change if needed)
data = pd.read_csv('ProcessedData_.csv')

def display_box_plot():
    # Create a tkinter window
    root = tk.Tk()
    root.title("Select Vehicle Types")
    root.geometry("300x300")

    # List of valid vehicle types
    valid_vehicle_types = ['Mid-Sized Sedan', 'SUV', 'Sports Car', 'Luxury Sedan', 'MPV', 'Hatchback','Stationwagon']

    # Create checkboxes for each vehicle type
    checkboxes = []
    for vehicle_type in valid_vehicle_types:
        var = tk.IntVar()
        checkbox = tk.Checkbutton(root, text=vehicle_type, variable=var)
        checkbox.pack(anchor=tk.W)
        checkboxes.append((vehicle_type, var))

    def get_selected_types():
        # Check if the input vehicle types are valid
        selected_types = [vehicle_type for vehicle_type, var in checkboxes if var.get() == 1]
        if not selected_types:
            messagebox.showerror("Error", "Please select at least one vehicle type.")
        else:
            filtered_data = data[data['Vehicle Type'].isin(selected_types)]
            filtered_data = filtered_data.sort_values(by='Depreciation') #arrange values of depreciation in ascendance


            # Calculate the first quartile (Q1)
            Q1 = filtered_data['Depreciation'].quantile(0.25)
            print(Q1)
            # Calculate the third quartile (Q3)
            Q3 = filtered_data['Depreciation'].quantile(0.75)
            print(Q3)
            # Calculate the interquartile range (IQR)
            IQR = Q3 - Q1

            # Define the upper and lower bounds for outliers
            upper_bound = Q3 + 1.5 * IQR
            lower_bound = Q1 - 1.5 * IQR

            # Remove outliers
            filtered_data = filtered_data[(filtered_data['Depreciation'] >= lower_bound) & (filtered_data['Depreciation'] <= upper_bound)]



            # displaying the chart
            sns.boxplot(x='Vehicle Type', y='Depreciation', data=filtered_data,showmeans=True)
            plt.xlabel('Vehicle Type')
            plt.ylabel('Depreciation')
            plt.title(f'Box Plot of Depreciation for {", ".join(selected_types)}')
            plt.show()
            root.destroy()

    button = tk.Button(root, text="Generate Plot", command=get_selected_types)
    button.pack()
    root.mainloop()

# Display the box plot for the specified vehicle type
display_box_plot()