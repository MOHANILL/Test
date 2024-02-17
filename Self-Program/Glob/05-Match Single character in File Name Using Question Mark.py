import glob

# path to search single character filename
path = "sales/?.jpg"
for file in glob.glob(path):
    print(file)

# path to search three-character filename
path = "sales/???.jpg"
for file in glob.glob(path):
    print(file)

# search file that starts with word 'cha' followed by exact two-character
path = "sales/cha*.txt"
for file in glob.glob(path):
    print(file)
