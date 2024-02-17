from tkinter import *
window = Tk()

window.title("Create Checkbox")
window.geometry("300x300+500+250")

chb1 = Checkbutton(window, text= "Mail")
chb1.pack()

chb2 = Checkbutton(window, text= "Femail")
chb2.pack()

chb3 = Checkbutton(window, text= "other")
chb3.pack()


window.mainloop()