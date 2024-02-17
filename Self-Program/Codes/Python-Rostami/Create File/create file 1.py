try:
    fp=open(r'C:\Users\AliMT\Desktop\Codes\Python-Rostami\Create File\3.txt')
    print("File is exites")
    print(fp.read())
    fp.close()
except IOError:
    print("File not found.Please chech the path.")
#finally:
#    print("Exit")
