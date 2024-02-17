import glob

# using glob to match every pathname
print('Inside current directory')
for item in glob.glob("*"):
    print(item)

# Match every files and folder from a given folder
print('Inside Sales folder')
for item in glob.glob("sales/*"):
    print(item)

print('All files starts with word march')
for item in glob.glob("sales/march*"):
    print(item)
