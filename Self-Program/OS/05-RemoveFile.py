# Python program to explain os.remove() method

# importing os module
import os

# File name
file = '01-file.txt'

# File location
location = "E:\ParentFolder\SubFolder"

# Path
path = os.path.join(location, file)

# Remove the file
# 'file.txt'
os.remove(path)
