from tkinter import *
window = Tk()

window.title("Create Text")
window.geometry("300x300+500+250")

text = Text(window, height = 15, width = 25)
text.pack()

text.insert(END, "hi \n salam be hame")


window.mainloop()
