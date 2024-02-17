# Opening the file with absolute path
fp = open(r'E:\ParentFolder\SubFolder\reports.txt', 'r')
# read file
print(fp.read())
# Closing the file after reading
fp.close()

# path if you using MacOs
# fp = open(r"/Users/myfiles/sample.txt", "r")
