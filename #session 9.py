#session 9
from    tkinter import *
window=Tk()
window.title("deleteed text")
window.geometry("700x7000+500+250")
def delete_text():
    text.delete("1.0", "end")
text=Text(window,heigh=20, width=30)
text.pack()
button1=Button(window ,text="DELETE",
cursor="heart",
relief=RIDGE,
activebackground="red",
font=("consolas",20),
state="normal",
command=delete_text)
button1.pack()
window.mainloop()