from tkinter import *
window = Tk()

window.title("Create Entry")
window.geometry("300x300+500+250")

entry1 = Entry(window, width=12, 
foreground = "red", 
background = "gray", 
font = ("Tahoma",20))

entry1.pack()

window.mainloop()