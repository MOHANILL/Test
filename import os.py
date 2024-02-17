
import time
""""
def shutdown(threshold=7):
    while time.gmtime().tm_hour < threshold:
        time.sleep(20) 
    os.system("shutdown /s /t 40")
"""
# import modules
from tkinter import *
import os
import time


# user define function
def shutdown():
	return os.system("shutdown /s /t 1")

def restart():
	return os.system("shutdown /r /t 1")

def logout():
	return os.system("shutdown -l")


# tkinter object
master = Tk()

#background set to purple
master.configure(bg='purple')
#while True:
#   if(datetime.datetime.utcnow()==9):
#       break
Button(master, text="Shutdown", command=shutdown).grid(row=0)
Button(master, text="Restart", command=restart).grid(row=1)
Button(master, text="Log out", command=logout).grid(row=2)

mainloop()