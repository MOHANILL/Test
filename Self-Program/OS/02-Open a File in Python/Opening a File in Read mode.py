try:
    fp = open("sample.txt", "r")
    # Reading the contents of the file and closing
    print(fp.read())
    fp.close()
except IOError:
    print("Please check the path.")
