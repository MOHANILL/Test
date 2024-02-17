from tkinter import *
window = Tk()

window.title("Create LsitBox")
window.geometry("300x300+500+250")

listbox1 = Listbox(window, height = 20, width = 15, fg = "blue")
listbox1.insert(1, "python")
listbox1.insert(2, "javascript")
listbox1.insert(3, "php")
listbox1.insert(4, "ruby")
listbox1.insert(5, "perl")
listbox1.insert(6, "assembly")

listbox1.pack()

window.mainloop()