from tkinter import *
window = Tk()

window.title("Create Radiobutton")
window.geometry("300x300+500+250")

rbtn = Radiobutton(window, text= "One")
rbtn.pack()
 
Radiobutton(window, text= "Two").pack() # secound method


window.mainloop()