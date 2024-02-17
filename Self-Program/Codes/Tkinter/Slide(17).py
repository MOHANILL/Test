from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("300x300")
def check():

         e_name = ename.get()
         c_name = cname.get()

         if c_name == "Male":

                l2=Label(win,text="Hello MR."+e_name).grid()
         elif c_name == "Femail":
                l2=Label(win,text="Hello MS."+e_name).grid()

l=Label(win, text="Enter Name:")
l.grid()
ename=StringVar()
e = Entry (win, width=10 , textvariable=ename)
e.grid()
cname=StringVar()
c = ttk.Combobox(win,width=15,values=("Male","Femail"),textvariable=cname)
c.grid()
b=Button(win,text="hello",command=check)
b.grid()
win.mainloop()
