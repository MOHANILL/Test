import glob

print("All pdf and txt files")
extensions = ('*.pdf', '*.jpg')
#print(type(extensions))==>tuple
files_list = []
for ext in extensions:
    files_list.extend(glob.glob(ext))
print(files_list)
