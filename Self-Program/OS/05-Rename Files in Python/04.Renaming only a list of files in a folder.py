"""Renaming only a list of files in a folder
While renaming files inside a folder, sometimes we may have to rename only a list of files,
 not all files. The following are the steps we need to follow for renaming only a set of files inside a folder.

Providing the list of files that needs to be renamed
Iterate through the list of files in the folder containing the files
Check if the file is present in the list
If present, rename the file according to the desired convention. Else, move to the next fileold"""
import os

files_to_rename = ['ana_2.txt', 'ana_9.txt']
folder = r"C:\Users\AliMT\Desktop\Self-Program\OS\05-Rename Files in Python\files\\"

# Iterate through the folder
for file in os.listdir(folder):
    # Checking if the file is present in the list
    if file in files_to_rename:
        # construct current name using file name and path
        old_name = os.path.join(folder, file)
        # get file name without extension
        only_name = os.path.splitext(file)[0]

        # Adding the new name with extension
        new_base = only_name + '_new' + '.txt'
        # construct full file path
        new_name = os.path.join(folder, new_base)

        # Renaming the file
        os.rename(old_name, new_name)

# verify the result
res = os.listdir(folder)
print(res)
