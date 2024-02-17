from tkinter import *
window = Tk()

window.title("Create Label")
window.geometry("300x300+500+250")

label1 = Label(window, text = "Hello World!!", bg = "black", 
fg = "yellow", 
cursor = "hand2", 
font = ("Consolas", 16) )
label1.pack()

window.mainloop()