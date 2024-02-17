import glob
import os

# Searching pattern inside folders and sub folders recursively
# search all jpg files
pattern = r"C:\Users\AliMT\Desktop\Self-Program\OS\**\*.jpg"
for item in glob.iglob(pattern, recursive=True):
    # delete file
    print("Deleting:", item)
    os.remove(item)

# Uncomment the below code check the remaining files
# print(glob.glob(r"E:\demos\files_demos\reports\**\*.*", recursive=True))
