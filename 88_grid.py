#grid() = geometry manager that organizes widgets in a table-like structure in a parent widget

from tkinter import *

def submit():
    print(firstNameEntry.get())
    print(lastNameEntry.get())
    print(emailNameEntry.get())

window = Tk()

titleLable = Label(window, text="Enter your info", font=("Arial", 25))
titleLable.grid(row=0, column=0, columnspan=2)

firstNamelabel = Label(window, text="First name: ", width=20, bg="red")
firstNamelabel.grid(row=1, column=0)
firstNameEntry = Entry(window)
firstNameEntry.grid(row=1, column=1)

lastNamelabel = Label(window, text="Last name: ", bg="green")
lastNamelabel.grid(row=2, column=0)
lastNameEntry = Entry(window)
lastNameEntry.grid(row=2, column=1)

emailNamelabel = Label(window, text="Email: ", bg="blue", width=30)
emailNamelabel.grid(row=3, column=0)
emailNameEntry = Entry(window)
emailNameEntry.grid(row=3, column=1)

submitButton = Button(window, text="Submit", command=submit)
submitButton.grid(row=4, column=0, columnspan=2)

window.mainloop()
