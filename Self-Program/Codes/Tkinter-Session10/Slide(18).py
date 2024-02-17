from tkinter import *
import os

window = Tk()
window.geometry("200x50")
window.resizable(0,0)
window.title("Kill")

def shut_down():
    os.system("shutdown /s /t 1")

def Restart():
    os.system("shutdown /r /t 1")

lable1 = Label(window, text="Click on button:  ")
lable1.grid()

button1 = Button(window,text="Shutdown",command=shut_down,bg="yellow")
button1.grid()

button2 = Button(window,text="Restart",command=shut_down,bg="red")
button2.grid(ipadx=10,column=2,row=1)

window.mainloop()
