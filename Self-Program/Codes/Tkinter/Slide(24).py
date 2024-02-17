import smtplib 
from tkinter import *
from tkinter import ttk, messagebox
import os

window = Tk()

window.title("Send Mail SMTP")

window.geometry('1250x680')
window.resizable(False, False)


def getTextInput():
    message = text.get("1.0", "end")
    send_mail(sender, receiver, password,message)
    

def send_mail(sender, receiver, password, message):
    sender_email = sender.get()
    sender_password = password.get()
    receivere_mail = receiver.get()

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, sender_password)
        s.sendmail(sender_email, receivere_mail, message)
        messagebox.showinfo("SendMessage", "Sent successfully")
        s.quit()
    except:
        messagebox.showinfo("SendMessage", "Error")
    

    


# Sender Address
l1 = Label(window, text="Sender Address: ",
          fg="black", font=("Consolas", 20))
l1.grid(row = 1, padx = 5, pady = 10)
sender = StringVar()
e1 = Entry(window, width=20, font=("Consolas", 20), textvariable=sender)
e1.grid(row = 1, column= 2)
# Sender Password
l2 = Label(window, text="Sender Password: ",
           fg="black", font=("Consolas", 20))
l2.grid(row=2, padx=5, pady=10)
password = StringVar()
e2 = Entry(window, width=20, font=("Consolas", 20), textvariable=password)
e2.grid(row=2, column=2)
# Receiver Address
l3 = Label(window, text="Receiver Address: ",
           fg="black", font=("Consolas", 20))
l3.grid(row=3, padx=5, pady=10)
receiver = StringVar()
e3 = Entry(window, width=20, font=("Consolas", 20), textvariable=receiver)
e3.grid(row = 3, column= 2)

# Message
l4 = Label(window, text="Message Text: ",
           fg="black", font=("Consolas", 20))
l4.grid(row=5, padx=5, pady=10)
message = StringVar()
text = Text(window, height=10, width=50, font=(
    "Consolas", 20))
text.grid(row=6, column = 2, padx=5, pady=10)
# Send Button
b = Button(window, text="Send", bg="orange",
           font=("Consolas", 16), command=getTextInput)
b.grid(row=7, column=2, padx=5, pady=10)
window.mainloop()
