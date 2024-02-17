#session9-4
from tkinter import *
from socket import *
window=Tk()
window.title("Find Website Ip Adress")
window.geometry('350x200')
def find_ip():
    ip=n.get()
    try:
        davaz.configure(text=gethostbyname(ip),fg="green")
    except:
        davaz.configure(text="Website URL is incorrect",fg="red")
I=Label(window, text="Enter website URL:",fg="red", bg="black", font=("consolas",20))
I.pack()
n=StringVar()
e=Entry(window,width=20,font=("consolas",20),textvariable=n)
e.pack()
b=Button(window,text="check", bg="orange",font=("consolas",20), command=find_ip)
b.pack()
davaz=Label(window,text="",fg="green",bg="black",font=("consolas",20))
davaz.pack()
window.mainloop()
