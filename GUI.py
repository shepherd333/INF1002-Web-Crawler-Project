import datetime
from tkinter import *
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
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

main = Tk()
main.title('Car Price History')
main.geometry('1000x700')
main.resizable()


data = pd.read_csv(r"ProcessedData.csv")

def year():
    os.system('averagePriceByYear.py')

def brand():
    os.system('averagePriceByBrand.py')

def depreciation():
    os.system('depreciation.py')


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
left_frame.place(x=0, y=30, relheight=1, relwidth=0.4)

#center_frame = Frame(main, bg=cf_bg)
#center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)

right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

# Placing components in the left frame
Label(left_frame, text="Vehicle History", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.05)
# Button(left_frame, text='View comparison', font=labelfont, command=lambda: show_image("Chart.png") , width=15).place(relx=0.1, rely=0.35)
Button(left_frame, text='View Average Price by Year', font=labelfont, command=year, width=30).place(relx=0.1, rely=0.35)
Button(left_frame, text='View Average Price by Brand', font=labelfont, command=brand, width=30).place(relx=0.1, rely=0.45)
Button(left_frame, text='View Vehicle Depreciation', font=labelfont, command=depreciation, width=30).place(relx=0.1, rely=0.55)

# Display image in right_frame
#Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5)


# Finalizing the GUI window
main.update()
main.mainloop()

