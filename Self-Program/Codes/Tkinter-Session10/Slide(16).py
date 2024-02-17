from tkinter import *
from socket import *

window = Tk()

window.title("Find Website Ip Address")

window.geometry('350x200')

def find_ip():
    ip = n.get()
    try:
        l2.configure(text= gethostbyname(ip),fg = "green")
    except:
        l2.configure(text= "Website URl is incorrect", fg = "red")
  
l = Label(window, text = "Enter Website URL: ", fg = "red", bg = "black", font = ("Consolas",20))
l.pack()

n = StringVar()

e = Entry(window, width=20, font = ("Consolas",20), textvariable=n)
e.pack()

b = Button(window, text = "Check", bg = "orange", font = ("Consolas",20), command = find_ip)
b.pack()

l2 = Label(window, text="", fg = "green",bg = "black",font = ("Consolas",20))
l2.pack()

window.mainloop()