from tkinter import *
window = Tk()

window.title("insert text to textwidget")
window.geometry("300x300+500+250")

def insert_text():
    text.insert(END, "hi \n Arjang")

button1 = Button(window, text = "Click!",
cursor= "heart", 
relief = RIDGE, 
activebackground = "green", 
font = ("Consolas",20), 
state = "normal" ,
command = insert_text)
button1.pack()

text = Text(window, height = 20, width = 30)
text.pack()

window.mainloop()
