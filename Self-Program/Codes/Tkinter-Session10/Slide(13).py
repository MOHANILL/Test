from tkinter import *
window = Tk()

window.title("Scrollbar")
window.geometry("300x150+500+250")


text = Text(window, height = 20, width = 30)
text.pack()
scroll = Scrollbar(window)

text.pack(side=LEFT, fill=Y)
scroll.pack(side=RIGHT, fill=Y)

scroll.config(command = text.yview)
text.config(yscrollcommand= scroll.set)

par = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"""

text.insert(END,par)

window.mainloop()