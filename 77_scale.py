from tkinter import *

def submit():
    print("Temperature is: "+str(scale.get())+ " degrees c")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL, 
              font=('Consolas',20),
              tickinterval=10, #adds numeric indicators for value
              showvalue=1, #0-hides current value
              resolution=5, #increment od slider
              troughcolor='blue',
              fg='red',
              bg='black'
              )

scale.set(((scale['from']-scale['to']) /2) + scale['to']) #presets to value of scale to mid
scale.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()