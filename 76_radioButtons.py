# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("Pizza!")
    elif(x.get()==1):
        print("Hamburger!")
    elif(x.get()==2):
        print("Hotdog!")
    else:
        print("Huh?")

window = Tk()

hamburger = PhotoImage(file='images\hamburger.png')
hotdog = PhotoImage(file='images\hotdog.png')
pizza = PhotoImage(file='images\pizza.png')
foodImages = [pizza,hamburger,hotdog]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x, #group radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value
                              padx=25, #adds padding on x-axis
                              font=('Impact',30),
                              image=foodImages[index], #adds images to radiobutton
                              compound="left", #aads image & text (left-side)
                              indicatoron=0, #eliminate circle indicators
                              width=375, #sets width of radio buttons 
                              command=order #set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W) #anchor aligns all radiobutton 


window.mainloop()