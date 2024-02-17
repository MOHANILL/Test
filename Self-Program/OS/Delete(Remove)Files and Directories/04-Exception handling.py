import os

file_path = r'C:\Users\AliMT\Desktop\Self-Program\OS\Delete(Remove)Files and Directories\Files\2.txt'
try:
    os.remove(file_path)
    print("Deleted File !")
except:
    print("The system cannot find the file specified")
    # your code
