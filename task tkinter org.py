# import mudules
import os
from tkinter import *
from tkinter import ttk


# create tkinter
win = Tk()
win.geometry("300x300")


def check():
# get path from user      
      path = ename.get()
      format1 = cname.get()
      folder_path="{path1}".format(path1=path)
      folder_path=r"{}".format(folder_path)
      test = os.listdir(folder_path)


# format managment
      if format1 == "                                        txt":
            for files in test:
                  if files.endswith(".txt"):
                        os.remove(os.path.join(folder_path, files))  
            print("Done")       
      elif format1 == "                                        jpg":
            for files in test:
                  if files.endswith(".jpg"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")
      elif format1 =="                                        png" :
            for files in test:
                  if files.endswith(".png"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")
      elif format1 == "                                        pdf":
            for files in test:
                  if files.endswith(".pdf"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")
      elif format1 == "                                        py":
            for files in test:
                  if files.endswith(".py"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")
      elif format1 =="                                        exe" :
            for files in test:
                  if files.endswith(".exe"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")
      elif format1 == "                                        dll":
            for files in test:
                     if files.endswith(".dll"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")
      elif format1 == "                                        log":
            for files in test:
                     if files.endswith(".log"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")
      elif format1 == "                                        mkv":
            for files in test:
                  if files.endswith(".mkv"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")
      elif format1 == "                                        mp3":
            for files in test:
                  if files.endswith(".mp3"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")
      elif format1 == "                                        mp4":
            for files in test:
                  if files.endswith(".mp4"):
                        os.remove(os.path.join(folder_path, files))
            print("Done")


# tkinter management
l=Label(win, text="Enter your path:")
l.grid()
ename=StringVar()
e = Entry (win ,width=10 , textvariable=ename)
e.grid()
s=Label(win,text="Select your format:")
s.grid()
cname=StringVar()
c = ttk.Combobox(win,width=40,values=("                                        log","                                        dll","                                        py","                                        txt","                                        jpg","                                        png","                                        pdf","                                        exe","                                        mkv","                                        mp3","                                        mp4",),textvariable=cname)
c.grid()
b=Button(win,text="enter",command=check)
b.grid()
win.mainloop()