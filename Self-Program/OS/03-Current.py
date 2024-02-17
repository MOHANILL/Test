import os
directory="GeeksforGeeks"
parent_dir="C:/ParentFolder"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)
directory = "Geeks"

# Parent Directory path
parent_dir = "D:/Pycharm projects"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)
