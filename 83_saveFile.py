from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\divya\\OneDrive\\Desktop\\python",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file",".html"),
                                        ("all files",".*")
                                    ])
    if file is None:
        return
    
    # filetext = str(text.get(1.0,END))
    filetext = input("Enter some text U guess: ")
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()