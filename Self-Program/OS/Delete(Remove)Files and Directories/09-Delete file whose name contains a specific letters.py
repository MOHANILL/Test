import glob
import os

# search files like abc.txt, abd.txt
pattern = r"C:\Users\AliMT\Desktop\Self-Program\OS\Delete(Remove)Files and Directories\Files\New folder[a-g]*.txt"
print(pattern)
for item in glob.iglob(pattern, recursive=True):
    os.remove(item)
