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
main.geometry('1300x800')
main.resizable()


data = pd.read_csv("ProcessedData.csv")

def year():
    os.system('averagePriceByYear.py')


def brand():
    os.system('averagePriceByBrand.py')


def depreciation():
    os.system('depreciation.py')


def csv_view():
    with open('ProcessedData.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Read the header row
        tree.delete(*tree.get_children())  # Clear the current data

        tree["height"] = 30
        tree["columns"] = header
        for i in header:
            tree.heading(i, text=i)
            max_width = max(data[i].astype(str).apply(len).max(), len(i))
            tree.column(i,width=max_width*18,anchor='c')
        for row in csv_reader:
            tree.insert("","end",values=row)



# def show_image(Imagefile):
#     image = ImageTk.PhotoImage(file=Imagefile)
#     label = (Label(right_frame, image=image))
#     label.image = image
#     label.grid(row=0, column=0, padx=5, pady=5)
#     return label


# Creating the background and foreground color variables
lf_bg = 'DeepSkyBlue' # bg color for the left_frame
cf_bg = 'Aqua' # bg color for the center_frame

# Placing the components in the main window
Label(main, text="VEHICLE PRICE HISTORY TRACKER", font=headlabelfont, bg='DodgerBlue3').pack(side=TOP, fill=X)

left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)

# center_frame = Frame(main, bg=cf_bg)
# center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)

right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.8)

# Placing components in the centre frame

# Placing components in right_frame
# l1 = tk.Label(right_frame, text="Search",font=labelfont,bg='Gray35',width=5)
# l1.grid(row=1,column=1,padx=1,pady=4)
# e1 = tk.Entry(right_frame,width=35,bg='white',font=labelfont)
# e1.grid(row=1,column=2,padx=1)
b1 = tk.Button(right_frame,text="Show Data",font=labelfont,bg='white',width=10,height=1, command=csv_view)
b1.grid(row=1,column=1,padx=3,pady=3)
tree = ttk.Treeview(right_frame,show="headings")
tree.grid(row=2,column=1,columnspan=18)
scrollbar = ttk.Scrollbar(right_frame,orient="horizontal",command=tree.xview)
scrollbar.grid(row=3,column=1,columnspan=10,sticky=tk.EW,padx=5,pady=5)
tree['xscrollcommand'] = scrollbar.set


# Placing components in the left frame
Label(left_frame, text="Vehicle History Charts", font=('Calibri',16), bg=lf_bg).place(relx=0.1, rely=0.05)
# Button(left_frame, text='View comparison', font=labelfont, command=lambda: show_image("Chart.png") , width=15).place(relx=0.1, rely=0.35)
Button(left_frame, text='View Average Price by Year', font=labelfont, command=year, width=22).place(relx=0.05, rely=0.15)
Button(left_frame, text='View Average Price by Brand', font=labelfont, command=brand, width=22).place(relx=0.05, rely=0.25)
Button(left_frame, text='View Vehicle Depreciation', font=labelfont, command=depreciation, width=22).place(relx=0.05, rely=0.35)

# Finalizing the GUI window
main.update()
main.mainloop()

