import glob
import os

# Delete file whose name starts with string 'pro'
pattern = r"C:\Users\AliMT\Desktop\Self-Program\OS\Delete(Remove)Files and Directories\Files\pro*"
for item in glob.iglob(pattern, recursive=True):
    os.remove(item)
