import os
old_name=r"C:\Users\AliMT\Desktop\Self-Program\OS\05-Rename Files in Python\a.txt"
new_name=r"C:\Users\AliMT\Desktop\Self-Program\OS\05-Rename Files in Python\new_a.txt"
# enclosing inside try-except
try:
    os.rename(old_name,new_name)
except FileExistsError:
    print("File already Exists")
    print("Removing existing file")
    os.remove(new_name)
    os.rename(old_name,new_name)
    print('Done renaming a file')
