from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x300")

tabcontrol = ttk.Notebook(win)

tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text = "Tab1")

tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab2, text = "Tab2")
tabcontrol.grid()

l = Label(tab1, text = "Hello World!!")
l.grid()

b = Button(tab2, text = "Start", bg = "yellow")
b.grid(ipadx=6,ipady=4)

win.mainloop()
