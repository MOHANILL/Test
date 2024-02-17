# Python program to explain os.rmdir() method

# importing os module
import os

# Directory name
directory = "Geeks"
	
# Parent Directory
parent = "E:\ParentFolder"

# Path
path = os.path.join(parent, directory)

# Remove the Directory
# "Geeks"
os.rmdir(path)
