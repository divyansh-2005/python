from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='This is an info message box',
    #                     message="You are a person")
    # while(True):
    #     messagebox.showwarning(title='WARNING!',
    #                         message="You have a VIRUS!!!!")
    # messagebox.showerror(title='ERROR',
    #                     message="something went wrong :(")

    # if messagebox.askokcancel(title='ask ok cancle',
    #                        message='Do you want to do the thing'):
    #     print('You did a thing!')
    # else:
    #     print('You canceled a thing')

    # if messagebox.askretrycancel(title='ask ok cancle',
    #                        message='Do you want to do retry the thing'):
    #     print('You retried a a thing!')
    # else:
    #     print('You canceled a thing')

    # if messagebox.askyesno(title='ask yes or no',
    #                     message='Do you like cake?'):
    #     print("I like cake too")
    # else:
    #     print('Why do you not like a cake')

    # answer = messagebox.askquestion(title="ask question",
    #                        message='Do you like pie?')
    # if(answer == 'yes'):
    #     print('I like pie too')
    # else:
    #     print('Why do you not like pie?')

    answer = messagebox.askyesnocancel(title='yes no cancle',
                              message='Do you like to code?',
                              icon='warning')
    if(answer==True):
        print('You like to code')
    elif(answer==False):
        print("then what")
    else:
        print('you have nothing to say')

window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()