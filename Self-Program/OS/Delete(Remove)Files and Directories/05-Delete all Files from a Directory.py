"""Sometimes we want to delete all files from a directory without deleting a directory.
Follow the below steps to delete all files from a directory.

Get the list of files in a folder using os.listdir(path) function.
It returns a list containing the names of the files and folders in the given directory.
Iterate over the list using a for loop to access each file one by one
Delete each file using the os.remove()"""
import os

path = r"C:\Users\AliMT\Desktop\Self-Program\OS\Delete(Remove)Files and Directories\Files\\"
for file_name in os.listdir(path):
    # construct full file path
    file = path + file_name
    if os.path.isfile(file):
        print('Deleting file:', file)
        os.remove(file)
