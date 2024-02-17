from tkinter import *
import os
import time

window = Tk()
window.title("Ping")
window.geometry('500x350')

def ping_ip():
    ip = n.get()
    ping = os.system("ping " + ip)
    if ping == 0:
        out = "Live!!"
    else:
        out = "Dead!!"
    text.insert(END, f"""
    -----------------------------
    {ip} is {out}
    -----------------------------
    """)

l = Label(window, text="Enter the IP: ",
          fg="red", bg="black", font=("Consolas", 20))
l.pack()
n = StringVar()
e = Entry(window, width=20, font=("Consolas", 20), textvariable=n)
e.pack()
b = Button(window, text="Check", bg="orange",
           font=("Consolas", 20), command=ping_ip)
b.pack()
text = Text(window, height = 10, width = 50)
text.pack()
window.mainloop()
