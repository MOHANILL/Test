import os


# getting the filename from the user
os.chdir("C:\\")
file_path = input("Enter filename:- ")

# checking whether file exists or not
if os.path.exists(file_path):
    # removing the file using the os.remove() method
    os.remove(file_path)
else:
    # file not found message
    print("File not found in the directory")

