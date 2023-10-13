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


headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 12)

main = Tk()
main.title('Car Price History')
main.geometry('1920x1080')
#main.configure(bg="red")




data = pd.read_csv("ProcessedData.csv")

def new_window():
    new_window = tk.Toplevel(main)
    new_window.title(f"DATA VIEWER")
    new_window.geometry("1920x1080")
    label = tk.Label(new_window, text=f"VIEW DATASET")
    label.pack()

    def csv_view():
        with open('ProcessedData.csv', 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            tree.delete(*tree.get_children())  # Clear the current data

            tree["height"] = 35
            tree["columns"] = header
            for i in header:
                tree.heading(i, text=i)
                tree.column(i,anchor='c')
            for row in csv_reader:
                tree.insert("", "end", values=row)

    open_button = tk.Button(new_window, text="View Data", command=csv_view)
    open_button.pack(pady=10)
    tree = ttk.Treeview(new_window,show='headings')
    hscrollbar = ttk.Scrollbar(new_window, orient='horizontal', command=tree.xview)
    tree.config(xscrollcommand=hscrollbar.set)
    tree.pack(fill="both")
    hscrollbar.pack(fill="x")


def year():
    os.system('averagePriceByYear.py')


def brand():
    os.system('averagePriceByBrand.py')


def depreciation():
    os.system('depreciation.py')


toplabel=tk.Label(main, text="VEHICLE PRICE HISTORY TRACKER", font=headlabelfont, bg='DodgerBlue3').pack(side=TOP, fill=X)
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
# # Finalizing the GUI window
main.mainloop()

