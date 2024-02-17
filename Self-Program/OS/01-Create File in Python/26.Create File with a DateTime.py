"""
Let’s see how to create a text file with the current date as its name.
Use the datetime module to get the current date and time and assign it to the file name to create a file with the date and time in its name.

Python provides a datetime module that has several classes to access and manipulate the date and timestamp value.
First, get the current datetime value
Next, we need to format datetime into a string to use it as a file name.
At last, pass it to the open() function to create a file
"""
from datetime import datetime

# get current date and time
x = datetime.now()

# create a file with date as a name day-month-year
file_name = x.strftime('%d-%m-%Y.txt')
with open(file_name, 'w') as fp:
    print('created', file_name)

# with name as day-month-year-hours-minutes-seconds
file_name_2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_2, 'w') as fp:
    print('created', file_name_2)

# at specified directory
file_name_3 = r"C:\Users\AliMT\Desktop\Self-Program\OS\01-Create File in Python\Backup\\" + x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_3, 'w') as fp:
    print('created', file_name_3)
