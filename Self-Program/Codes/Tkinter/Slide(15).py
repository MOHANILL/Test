from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("Message Box")

window.geometry('350x200')

def clicked():

    res = messagebox.askyesno('Message title','This is A Message')

btn = Button(window,text='Click here', command=clicked)

btn.grid(column=0,row=0)

window.mainloop()
