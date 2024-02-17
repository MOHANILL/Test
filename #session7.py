#session7
"""
from datetime import datetime
#get current data and time
x=datetime.now()
#creat a file with data as aname day-month-year
file_name=x.strftime('%d-%m-%Y.txt')
with open (file_name,'w') as fp:
    print('created', file_name)
#with name as day-month-year-hours-minuts-seconds
file_name_2=x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_2,'w') as fp:
    print('created', file_name_2)
#at specified directory
file_name_3=r"F:\python learn\BP\\"+x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open (file_name_3,'w') as fp:
    print('created',file_name_3)
"""
##
#opening the file with relative path
try:
    fp=open("reports.txt","r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("File Not found please check the path")
##
with open('soli.txt','r') as file:
    #read first 3 line:
    for i in range(3):
        print(file.readline().strip())
##
import os
old_name=r"F:\python learn\BP\roozi.txt"
new_name=r"F:\python learn\BP\soli.txt"
if(os.path.isfile(new_name)):
    print("The file already exist")
else:
    #rename the file name
    os.rename(old_name, new_name)
    print("changed!!")