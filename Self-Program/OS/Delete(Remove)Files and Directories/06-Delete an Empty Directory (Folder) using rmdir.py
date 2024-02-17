import os

# Deleting an empty folder
directory = r"C:\Users\AliMT\Desktop\Self-Program\OS\Delete(Remove)Files and Directories\Files\New folder"
os.rmdir(directory)
print("Deleted '%s' directory successfully" % directory)
