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


headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 12)

main = Tk()
main.title('Car Price History')
main.geometry('1920x1080')
#main.configure(bg="red")

data = pd.read_csv("ProcessedData.csv")


def new_window():
    new_win = tk.Toplevel(main)
    new_win.title(f"DATA VIEWER")
    new_win.geometry("1920x1080")
    label = tk.Label(new_win, text=f"VIEW DATASET")
    label.pack()

    def csv_view():
        with open('ProcessedData.csv', 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            tree.delete(*tree.get_children())  # Clear the current data

            tree["height"] = 25
            tree["columns"] = header
            for i in header:
                tree.heading(i, text=i)
                tree.column(i,anchor='c')
            for row in csv_reader:
                tree.insert("", "end", values=row)
    def filtered_csv_view():
        with open('ProcessedData.csv', 'r') as file:
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
            max_price = float(max_price_entry.get())
            filtered_data = data[(data['Brand'] == brand) &
                               (data['Vehicle Type'] == v_type) &
                               (data['Transmission'] == v_trans) &
                                (data['Price'] <= max_price)]
            filter_data(filtered_data)

    def filter_data(filtered_data):
        for item in tree.get_children():
            tree.delete(item)
        if not filtered_data.empty:
            for index, row in filtered_data.iterrows():
                tree.insert('', 'end', values=row.tolist())


    def machine_learn():
        os.system('carMartML.py')

    open_button = tk.Button(new_win, text="View All Data", command=csv_view)
    open_button.pack(pady=10)
    tree = ttk.Treeview(new_win, show='headings')
    hscrollbar = ttk.Scrollbar(new_win, orient='horizontal', command=tree.xview)
    tree.config(xscrollcommand=hscrollbar.set)
    tree.place(x=150,y=100,width=1200,height=600)
    hscrollbar.place(x=150,y=700,width=1200)
    ml_Button = tk.Button(new_win, text="Predict Price", command=machine_learn)
    ml_Button.place(x=500,y=720)

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

    tk.Label(new_win, text='Maximum Price:').place(x=120,y=70)
    max_price_entry = tk.Entry(new_win)
    max_price_entry.place(x=220,y=70)

    filter_button = tk.Button(new_win, text="Filter", command=filtered_csv_view)
    filter_button.place(x=390,y=10)


def year():
    os.system('averagePriceByYear.py')


def brand():
    os.system('averagePriceByBrand.py')


def depreciation():
    os.system('depreciation.py')


def coe_price_trend():
    os.system('COE_pricetrend.py')


def average_price_by_brand():
    os.system('zwTest2.py')


toplabel=tk.Label(main, text="VEHICLE PRICE", font=headlabelfont, bg='DodgerBlue3').pack(side=TOP, fill=X)
data_button = tk.Button(main, text="Show All Data", command=lambda: new_window(),bg='white')
data_button.pack(pady=10)


# Placing components in the main frame
Label(main,text="Vehicle History Charts", font=('Calibri',16)).pack(pady=20)
b2= tk.Button(main, text='View Average Price by Year', font=labelfont,bg='white', command=year, width=22)
b2.pack(padx=5,pady=10)
b3= tk.Button(main,text='View Average Price by Brand', font=labelfont, bg='white',command=brand, width=22)
b3.pack(padx=5,pady=10)
b4= tk.Button(main,text='View Vehicle Depreciation', font=labelfont,bg='white', command=depreciation, width=22)
b4.pack(padx=5,pady=10)
b5= tk.Button(main,text='View COE Price Trend', font=labelfont,bg='white', command=coe_price_trend, width=22)
b5.pack(padx=5,pady=10)
b6= tk.Button(main,text='View Average Price by Brand', font=labelfont,bg='white', command=average_price_by_brand, width=22)
b6.pack(padx=5,pady=10)
# # Finalizing the GUI window
main.mainloop()

