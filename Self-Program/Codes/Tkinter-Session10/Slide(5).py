from tkinter import *
window = Tk()

window.title("Create Button")
window.geometry("300x300+500+250")

button1 = Button(window, text = "Click!",
cursor= "hand1", 
relief = RIDGE, 
activebackground = "green", 
font = ("Consolas",12), 
state = "normal" )

button1.pack()

window.mainloop()