from tkinter import *

window = Tk()

count = 0

def click():
    global count
    count += 1
    print(count)
    print("you clicked the button")

photo = PhotoImage('logo.png')

button = Button(window,
                text="Click me",
                command=click,
                font=("comic Sans",30),
                fg="green",
                bg="black",
                activeforeground="green",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='top'                
)

button.pack()

window.mainloop()