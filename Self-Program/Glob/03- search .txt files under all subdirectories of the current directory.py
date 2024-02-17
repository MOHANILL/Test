import glob

# path to search file
path = '**/*.pdf'
for file in glob.glob(path, recursive=True):
    print(file)
