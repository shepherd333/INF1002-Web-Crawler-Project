from tkinter import *
from tkinter import filedialog
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import numpy as np
import os
import sys
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import xgboost as xgb
import pickle

# setting some fonts
headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 12)

# Main Tkinter GUI
main = Tk()
main.title('ONLINE USED CARS MARKETPLACE DATA AND ANALYSIS')
main.geometry('1920x1080')
# main.configure(bg="red")

# csv to be read and used as dataframe
data = pd.read_csv("ProcessedData_.csv")
# Load the trained XGBoost model
with open('model.pkl', 'rb') as f:
    xgr = pickle.load(f)


# second level GUI window
def new_window():
    new_win = tk.Toplevel(main)
    new_win.title(f"DATA VIEWER")
    new_win.geometry("1920x1080")
    label = tk.Label(new_win, text=f"VIEW VEHICLE DATASET")
    label.pack()

    # read csv and load into treeview
    def csv_view():
        with open('ProcessedData_.csv', 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # read the first row as headers
            tree.delete(*tree.get_children())  # Clear the current data

            tree["height"] = 25  # number of rows to display
            tree["columns"] = header
            for i in header:
                tree.heading(i, text=i)
                tree.column(i,anchor='c')  # for loop to insert headers
            for row in csv_reader:
                tree.insert("", "end", values=row)  # for loop to insert rows from csv

    def filtered_csv_view():  # almost the same as csv_view function but with filtered rows
        with open('ProcessedData_.csv', 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            tree.delete(*tree.get_children())  # Clear the current data

            tree["height"] = 25
            tree["columns"] = header
            for i in header:
                tree.heading(i, text=i)
                tree.column(i,anchor='c')
            brand = vehicle_brand_var.get()
            v_type = vehicle_type_var.get()
            v_trans = vehicle_transmission_var.get()
            min_price = float(min_price_entry.get())
            max_price = float(max_price_entry.get())
            filtered_data = data[(data['Brand'] == brand) &  # filtering rows based on user input
                               (data['Vehicle Type'] == v_type) &
                               (data['Transmission'] == v_trans) &
                                (data['Price'] >= min_price) &
                                (data['Price'] <= max_price)]
            filter_data(filtered_data)

    def filter_data(filtered_data):  # function to clear the treeview and replace with filtered data
        for item in tree.get_children():
            tree.delete(item)
        if not filtered_data.empty:
            for index, row in filtered_data.iterrows():
                tree.insert('', 'end', values=row.tolist())

    def predict_price():  # ML Model
        # Retrieve input values from the GUI
        omv = float(omv_entry.get())
        curb_weight = float(curb_weight_entry.get())
        road_tax = float(road_tax_entry.get())
        coe_price = float(coe_price_entry.get())
        no_of_owners = float(no_of_owners_entry.get())

        # Prepare input data for prediction
        input_data = pd.DataFrame({
            'Road Tax': [road_tax],
            'COE Left': 0,
            'Mileage': 0,
            'OMV': [omv],
            'COE Price': [coe_price],
            'Curb Weight': [curb_weight],
            'No. Of Owners': [no_of_owners]})

        # Make a prediction using the XGBoost model
        predicted_price = xgr.predict(input_data)
        predicted_value = predicted_price[0]

        # Display the predicted price
        result_label.config(text=f"Predicted Price: {predicted_value:.2f}")

        # Compare the predicted price to the user input price
        user_input_price = float(price_entry.get())

        if predicted_price < user_input_price:
            feedback_label.config(text="Predicted price is lower than the input price.")
        elif predicted_price == user_input_price:
            feedback_label.config(text="Predicted price is the same as the input price.")
        else:
            feedback_label.config(text="Predicted price is higher than the input price.")

    open_button = tk.Button(new_win, text="View All Data", command=csv_view)  # button to view full csv data
    open_button.pack(pady=10)
    tree = ttk.Treeview(new_win, show='headings')  # treeview to display the csv
    hscrollbar = ttk.Scrollbar(new_win, orient='horizontal', command=tree.xview)  # horizontal scrollbar to view treeview
    tree.config(xscrollcommand=hscrollbar.set)
    tree.place(x=150,y=100,width=1200,height=600)
    hscrollbar.place(x=150,y=700,width=1200)

    #  Enter unique values from columns in the csv to add into a dropdown list for user to choose
    unique_vehicle_brand = data['Brand'].unique()
    vehicle_brand = [vt.strip() for vt in unique_vehicle_brand if vt.strip() != '']
    tk.Label(new_win, text='Vehicle Brand:').place(x=120, y=10)
    vehicle_brand_var = tk.StringVar(new_win)
    vehicle_brand_dropdown = ttk.Combobox(new_win, textvariable=vehicle_brand_var, values=vehicle_brand)
    vehicle_brand_dropdown.place(x=220,y=10)

    unique_vehicle_type = data['Vehicle Type'].unique()
    vehicle_type = [vt.strip() for vt in unique_vehicle_type if vt.strip() != '']
    tk.Label(new_win, text='Vehicle Type:').place(x=120, y=30)
    vehicle_type_var = tk.StringVar(new_win)
    vehicle_type_dropdown = ttk.Combobox(new_win, textvariable=vehicle_type_var, values=vehicle_type)
    vehicle_type_dropdown.place(x=220,y=30)

    unique_vehicle_transmission = data['Transmission'].unique()
    vehicle_transmission = [vt.strip() for vt in unique_vehicle_transmission if vt.strip() != '']
    tk.Label(new_win, text='Transmission:').place(x=120, y=50)
    vehicle_transmission_var = tk.StringVar(new_win)
    vehicle_transmission_dropdown = ttk.Combobox(new_win, textvariable=vehicle_transmission_var, values=vehicle_transmission)
    vehicle_transmission_dropdown.place(x=220,y=50)

    #  User input fields for min and max price
    tk.Label(new_win, text='Minimum Price:').place(x=120,y=70)
    min_price_entry = tk.Entry(new_win)
    min_price_entry.place(x=220,y=70)

    tk.Label(new_win, text='Maximum Price:').place(x=350,y=70)
    max_price_entry = tk.Entry(new_win)
    max_price_entry.place(x=450,y=70)

    #  button to display the filtered csv data
    filter_button = tk.Button(new_win, text="Filter", command=filtered_csv_view)
    filter_button.place(x=390,y=10)

    #  Text label to tell users what the ML is  for
    ML_label = tk.Label(new_win, text="Interested in a car? Let's check if the deal is worth it!")
    ML_label.place(x=200,y=720)

    # Create input fields for ML model
    omv_label = tk.Label(new_win, text="OMV")
    omv_label.place(x=500,y=780)
    omv_entry = tk.Entry(new_win)
    omv_entry.place(x=500,y=800)

    curb_weight_label = tk.Label(new_win, text="Curb Weight")
    curb_weight_label.place(x=500,y=740)
    curb_weight_entry = tk.Entry(new_win)
    curb_weight_entry.place(x=500,y=760)

    road_tax_label = tk.Label(new_win, text="Road Tax")
    road_tax_label.place(x=350,y=740)
    road_tax_entry = tk.Entry(new_win)
    road_tax_entry.place(x=350,y=760)

    coe_price_label = tk.Label(new_win, text="COE Price")
    coe_price_label.place(x=350,y=780)
    coe_price_entry = tk.Entry(new_win)
    coe_price_entry.place(x=350,y=800)

    no_of_owners_label = tk.Label(new_win, text="No. Of Owners")
    no_of_owners_label.place(x=200,y=780)
    no_of_owners_entry = tk.Entry(new_win)
    no_of_owners_entry.place(x=200,y=800)

    price_label = tk.Label(new_win, text="Input Price")
    price_label.place(x=200,y=740)
    price_entry = tk.Entry(new_win)
    price_entry.place(x=200,y=760)

    # Create a button for prediction
    predict_button = tk.Button(new_win, text="Predict", command=predict_price)
    predict_button.place(x=650,y=780)

    # Create a label to display the predicted price
    result_label = tk.Label(new_win, text="")
    result_label.place(x=700,y=780)

    # Create a label to provide feedback on predicted price
    feedback_label = tk.Label(new_win, text="")
    feedback_label.place(x=700,y=800)


#  functions to call matplotlib files
def year():
    os.system('averagePriceByYear.py')


def brand():
    os.system('averagePriceByBrand.py')


def depreciation():
    os.system('depreciation.py')


def average_coe():
    os.system('averageCOE.py')


def coe_carprice():
    os.system('coeQuota_carPrice.py')


def coe_premium():
    os.system('coeQuota_premium.py')


def vehbyregdate():
    os.system('VehByRegDate.py')


def medianprice():
    os.system('medianPrice.py')



# Placing components in the main frame
toplabel=tk.Label(main, text="ONLINE USED CARS MARKETPLACE DATA AND ANALYSIS", font=headlabelfont, bg='AQUA').pack(side=TOP, fill=X)
data_button = tk.Button(main, text="Show All Data", command=lambda: new_window(),bg='white')
data_button.pack(pady=10)

Label(main,text="Vehicle Data Analysis Charts", font=('Calibri',16)).pack(pady=20)
b2= tk.Button(main, text='View Average Price by Year', font=labelfont,bg='white', command=year, width=30)
b2.pack(padx=5,pady=10)
b3= tk.Button(main,text='View Average Price by Brand', font=labelfont, bg='white',command=brand, width=30)
b3.pack(padx=5,pady=10)
b4= tk.Button(main,text='View Vehicle Depreciation', font=labelfont,bg='white', command=depreciation, width=30)
b4.pack(padx=5,pady=10)
b5= tk.Button(main,text='View Average COE Price', font=labelfont,bg='white', command=average_coe, width=30)
b5.pack(padx=5,pady=10)
b6= tk.Button(main,text='Annual COE Quotas vs Average Car Price', font=labelfont,bg='white', command=coe_carprice, width=30)
b6.pack(padx=5,pady=10)
b7= tk.Button(main,text='Annual COE Quotas vs Premium Price', font=labelfont,bg='white', command=coe_premium, width=30)
b7.pack(padx=5,pady=10)
b8= tk.Button(main,text='Number of Vehicles Registered by Year', font=labelfont,bg='white', command=vehbyregdate, width=30)
b8.pack(padx=5,pady=10)
b9= tk.Button(main,text='Median Price by Brands', font=labelfont,bg='white', command=medianprice, width=30)
b9.pack(padx=5,pady=10)

# Running the GUI window
main.mainloop()

