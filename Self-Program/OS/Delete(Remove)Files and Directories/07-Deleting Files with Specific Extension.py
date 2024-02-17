import glob
import os

# Search files with .txt extension in current directory
pattern = r"C:\Users\AliMT\Desktop\Self-Program\OS\Delete(Remove)Files and Directories\Files\*.jpg"
files = glob.glob(pattern)

# deleting the files with txt extension
for file in files:
    os.remove(file)
