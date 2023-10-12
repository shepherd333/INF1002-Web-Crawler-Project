import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox, ttk
from matplotlib.figure import Figure

data = pd.read_csv(r"C:\Users\tohzh\PycharmProjects\INF1002-Web-Crawler-Project\ProcessedData.csv")

# Preprocess the unique vehicle types
unique_vehicle_types = data['Vehicle Type'].unique()
vehicle_types = [vt.strip() for vt in unique_vehicle_types if vt.strip() != '']

def generate_bar_graph():
    min_price = float(min_price_entry.get())
    max_price = float(max_price_entry.get())
    vehicle_type = vehicle_type_var.get()

    # Filter data based on user input
    filtered_data = data[(data['Price'] >= min_price) & (data['Price'] <= max_price) & (data['Vehicle Type'] == vehicle_type)]

    if filtered_data.empty:
        messagebox.showinfo("No Data", "No data found for the given criteria.")
        return

    # Sort the data by price within each brand
    sorted_data = filtered_data.groupby('Brand')['Price'].mean().reset_index().sort_values(by='Price')

    # Generate bar graph
    fig = Figure(figsize=(12, 6))
    ax = fig.add_subplot(111)

    # Plotting prices for each brand
    for _, row in sorted_data.iterrows():
        brand_data = filtered_data[filtered_data['Brand'] == row['Brand']]
        ax.bar(brand_data['Brand'], brand_data['Price'], label=row['Brand'])

    ax.set_xlabel('Vehicle Model')
    ax.set_ylabel('Price')
    ax.set_title('Prices Sorted by Brand')
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)


# Create the main window
window = tk.Tk()
window.title('Interactive Bar Graph Generator')

# Labels and textboxes for user input
tk.Label(window, text='Minimum Price:').grid(row=0, column=0, padx=10, pady=5)
min_price_entry = tk.Entry(window)
min_price_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text='Maximum Price:').grid(row=1, column=0, padx=10, pady=5)
max_price_entry = tk.Entry(window)
max_price_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text='Vehicle Type:').grid(row=2, column=0, padx=10, pady=5)
vehicle_type_var = tk.StringVar(window)
vehicle_type_dropdown = ttk.Combobox(window, textvariable=vehicle_type_var, values=vehicle_types)
vehicle_type_dropdown.grid(row=2, column=1, padx=10, pady=5)

# Button to generate the bar graph
generate_button = tk.Button(window, text='Generate Bar Graph', command=generate_bar_graph)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
window.mainloop()
