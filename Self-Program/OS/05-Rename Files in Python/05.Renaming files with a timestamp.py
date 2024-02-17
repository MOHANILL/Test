"""Renaming files with a timestamp
In some applications, the data or logs will be stored in the files regularly in a fixed time interval.
It is a standard convention to append a timestamp to file name to make them easy for storing and using later.
 In Python, we can use the datetime module to work with dates and times.

Please follow the below steps to append timestamp to file name:

Get the current timestamp using a datetime module and store it in a separate variable
Convert timestamp into a string
Append timestamp to file name by using the concatenation operator
Now, rename a file with a new name using a os.rename()
Consider the following example where we are adding the timestamp in the “%d-%b-%Y” format ."""
import os
from datetime import datetime
# adding date-time to the file name
current_timestamp=datetime.today().strftime('%d-%b-%Y')
old_name=r"C:\Users\AliMT\Desktop\Self-Program\OS\05-Rename Files in Python\files\a.txt"
new_name=r"C:\Users\AliMT\Desktop\Self-Program\OS\05-Rename Files in Python\files\a"+current_timestamp+".txt"
os.rename(old_name,new_name)
