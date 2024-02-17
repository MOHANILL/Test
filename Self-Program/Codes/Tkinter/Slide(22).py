from tkinter import *
import os

window = Tk()
window.title("SearchFile")
window.geometry('500x350')
window.resizable(False,False)

def find_drive():
    drives = []
    for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if os.path.exists(f'{drive_letter}:'):
            drives.append(f'{drive_letter}:')
        else:
            pass
    find_file(drives) 
def find_file(drives):
    filename = n.get()
    result = []
    search_path = []

    for search_path in drives:
        for root, dir, files in os.walk(search_path):
            if filename in files:
                result.append(os.path.join(root, filename))
    if result == []:
        text.insert(END, f"""
------------------------------------------------
{filename} Not Find!!
------------------------------------------------
        """)
    else:
        text.insert(END, f"""
------------------------------------------------
{filename} Find:
{result}
------------------------------------------------
        """)

l = Label(window, text="Enter the File Name: ",
          fg="red", bg="black", font=("Consolas", 20))
l.pack()
n = StringVar()
e = Entry(window, width=20, font=("Consolas", 20), textvariable=n)
e.pack()
b = Button(window, text="Check", bg="orange",
           font=("Consolas", 20), command=find_drive)
b.pack()
text = Text(window, height=10, width=50)
text.pack()
window.mainloop()
