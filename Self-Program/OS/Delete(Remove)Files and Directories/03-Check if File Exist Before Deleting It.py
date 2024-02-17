import os

file_path = r'C:\Users\AliMT\Desktop\Self-Program\OS\Delete(Remove)Files and Directories\Files\1.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print("Deleted File !")
else:
    print("The system cannot find the file specified")
