import os
path_file=r"E:\ParentFolder\SubFolder\03-file.txt"
print(os.stat(path_file))
print(os.stat(path_file).st_size)
