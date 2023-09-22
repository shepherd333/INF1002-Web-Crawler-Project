import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk

headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

main = Tk()
main.title('Car Price Records')
main.geometry('1000x700')
main.resizable()

# Creating the background and foreground color variables
lf_bg = 'DeepSkyBlue' # bg color for the left_frame
cf_bg = 'Aqua' # bg color for the center_frame

# Placing the components in the main window
Label(main, text="VEHICLE PRICE HISTORY TRACKER", font=headlabelfont, bg='DodgerBlue3').pack(side=TOP, fill=X)

left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)

center_frame = Frame(main, bg=cf_bg)
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)

right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

# Placing components in the left frame
Label(left_frame, text="Vehicle Name", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.05)
Label(left_frame, text="Vehicle Model", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.18)
Label(left_frame, text="Vehicle Colour", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.31)
Label(left_frame, text="Category", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.44)
Label(left_frame, text="Current Price", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.57)
Label(left_frame, text="Whatever variable", font=labelfont, bg=lf_bg).place(relx=0.1, rely=0.7)

# Finalizing the GUI window
main.update()
main.mainloop()