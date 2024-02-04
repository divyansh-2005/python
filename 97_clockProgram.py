from tkinter import *
from time import *

def update():
    time_str = strftime("%I:%M:%S %p") 
    time_lable.config(text=time_str)

    day_str = strftime("%A") 
    day_lable.config(text=day_str)

    date_str = strftime("%B %d, %Y") 
    date_lable.config(text=date_str)

    window.after(1000,update)

window = Tk()

time_lable = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_lable.pack()

day_lable = Label(window,font=("Ink Free",25))
day_lable.pack()

date_lable = Label(window,font=("Ink Free",30))
date_lable.pack()

update()

window.mainloop()