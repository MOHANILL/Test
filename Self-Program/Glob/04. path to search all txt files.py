import glob

# path to search all txt files
path = "sales/*.jpg"
for file in glob.glob(path):
    print(file)
