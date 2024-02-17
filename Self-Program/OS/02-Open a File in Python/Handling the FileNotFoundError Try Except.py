try:
    fp = open(r'C:\Users\AliMT\Desktop\Self-Program\OS\01-Create File in Python\Backup\samples.txt', 'r')
    print(fp.read())
    fp.close()
except IOError:
    print("File not found. Please check the path.")
finally:
    print("Exit")
