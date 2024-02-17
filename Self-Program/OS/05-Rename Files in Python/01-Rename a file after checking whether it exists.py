import os
old_name=r"C:\Users\AliMT\Desktop\Self-Program\OS\05-Rename Files in Python\a.txt"
new_file=r"C:\Users\AliMT\Desktop\Self-Program\OS\05-Rename Files in Python\b.txt"
#Use the isfile(‘path’) function before renaming a file. It returns true if the destination file already exists.
if os.path.isfile(new_file):
    print("the file already exists")
else:
    #rename The filename
    os.rename(old_name,new_file)
    print("Changed !")
