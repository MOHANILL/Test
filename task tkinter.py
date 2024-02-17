import os
from tkinter import *
from tkinter import ttk
import glob
win = Tk()
win.geometry("300x300")

def check():
         
         path = ename.get()
         format1 = cname.get()
#az inja ******************************************************
         folder_path="{path1}".format(path1=path)
         folder_path=r"{}".format(folder_path)
         print(folder_path)
         
         
#ta inja moshkelemoone**************************************************



         
#dar vaqe ma too oon ghesmat ye variable taarif mikonim ke on ro be glob haye paiin bedim
         if format1 == "txt":
                os.remove((glob.glob(path_org)))
         elif format1 == "jpg":
                os.remove((glob.glob(path_org)))
         elif format1 == "png":
              test = os.listdir(folder_path)
              for images in test:
                     if images.endswith(".png"):
                         os.remove(os.path.join(folder_path, images))
         elif format1 == "pdf":
                os.remove((glob.glob(path_org)))
         elif format1 == "py":
                os.remove((glob.glob(path_org)))
         elif format1 == "exe":
                os.remove((glob.glob(path_org)))
         elif format1 == "dll":
                os.remove((glob.glob(path_org)))
         elif format1 == "log":
                os.remove((glob.glob(path_org)))
         elif format1 == "mkv":
                os.remove((glob.glob(path_org)))
         elif format1 == "mp3":
                os.remove((glob.glob(path_org)))
         elif format1 == "mp4":
                os.remove((glob.glob(path_org)))
l=Label(win, text="Enter your path:")
l.grid()
ename=StringVar()
e = Entry (win, width=10 , textvariable=ename)
e.grid()
cname=StringVar()
c = ttk.Combobox(win,width=40,values=("log","    dll","   py","    txt","    jpg","   png","   pdf","   exe","  mkv","  mp3","    mp4",),textvariable=cname)
c.grid()
b=Button(win,text="enter",command=check)
b.grid()
win.mainloop()
