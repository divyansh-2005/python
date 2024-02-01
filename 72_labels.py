from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

window.config(background="black")
# window.geometry("400x400")

photo = PhotoImage(file='logo.png')

label = Label(window, 
              text="Hello World", 
              font=('Arial',40,'bold'), 
              fg='green', 
              bg="pink",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
            #   image=photo,
            #   compound='bottom'
            )
label.pack()
# label.place(x=100,y=100)

window.mainloop()