from tkinter import *
from tkinter import ttk
import random 

win = Tk()
win.geometry("800x600")
def generator():

    lenght = lent.get()
    character = char.get()
         
    password=''
    
    for c in range(lenght):
        password += random.choice(character)
        
    text.insert(END, password + "\n")

def clear():
    text.delete("1.0", "end")

l1=Label(win, text="Password lenght : ", font = ("Consolas",20))
l1.grid()
lent =IntVar()
e1 = Entry (win, width=20 , font = ("Consolas",20), textvariable=lent)
e1.grid(column=2, row=0)

l2=Label(win, text="Characters : ", font = ("Consolas",20))
l2.grid(column=0, row=2)
char =StringVar()
e2 = Entry (win, width=20 , font = ("Consolas",20), textvariable=char)
e2.grid(column=2, row=2)

b=Button(win,text="generate", font = ("Consolas",20), command=generator)
b.grid(column=2, row=4)

text = Text(win, height = 20, width = 50, font = ("Consolas",12))
text.grid(column=2, row=6)

b=Button(win,text="Clear", font = ("Consolas",20), command=clear)
b.grid(column=2, row=7)

win.mainloop()
