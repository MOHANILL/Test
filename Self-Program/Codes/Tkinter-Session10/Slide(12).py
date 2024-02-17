from tkinter import *
window = Tk()

window.title("delete text")
window.geometry("300x500+500+250")

def delete_text():
    text.delete("1.0", "end")

text = Text(window, height = 20, width = 30)
text.pack()

button1 = Button(window, text = "DELETE",
cursor= "heart", 
relief = RIDGE, 
activebackground = "red", 
font = ("Consolas",20), 
state = "normal" ,
command = delete_text)
button1.pack()

window.mainloop()
