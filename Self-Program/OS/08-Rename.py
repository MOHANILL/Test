import os

# Absolute path of a file
old_name = r"E:\ParentFolder\SubFolder\02-file.txt"
new_name = r"E:\ParentFolder\SubFolder\03-file.txt"

# Renaming the file
os.rename(old_name, new_name)
