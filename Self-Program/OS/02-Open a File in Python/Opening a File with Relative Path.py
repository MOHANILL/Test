# Opening the file with relative path
try:
    fp = open("reports.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("File Not Found Please check the path.")
