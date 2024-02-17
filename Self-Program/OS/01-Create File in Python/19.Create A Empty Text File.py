#We don’t have to import any module to create a new file. We can create a file using the built-in function open().
#open('file_path','access_mode')
# create a empty text file
# in current directory
fp = open('sheyda.txt', 'x')
#Open a file only for exclusive creation. If the file already exists, this operation fails.
fp.close()
