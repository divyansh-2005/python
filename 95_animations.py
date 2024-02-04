from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

photo_image = PhotoImage(file='images\\ball.png')
myimage = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(myimage)
    print(coordinates)
    if(coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):
        xVelocity = -xVelocity
    if(coordinates[1] >= (HEIGHT-image_height) or coordinates[0] < 0):
        yVelocity = -yVelocity
    canvas.move(myimage,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()