"""
Renaming the Extension of the Files
We can change only the extension of
the files using the rename() method. This is done by getting
the list of the files and then get only the file name using
the splitext() method of the os module.

This method returns the root and extension separately.
Once we get the root/base of the filename, we can add
the new extension to it while renaming it using the rename() method

Use the below steps to rename only extension: –

Get List file names from a directory using a os.listdir(folder)
Next, Iterate each file from a list of filenames
Construct current file name using os.path.join() method by passing file name and path
Now, use the replace() method of a str class to replace an existing extension with a new extension in the file name
At last, use the os.rename() to rename an old name with a new name
"""
import os

folder = r"E:\ParentFolder\SubFolder\\"
# Listing the files of a folder
print('Before rename')
files = os.listdir(folder)
print(files)

# rename each file one by one
for file_name in files:
    # construct full file path
    old_name = os.path.join(folder, file_name)

    # Changing the extension from txt to pdf
    new_name = old_name.replace('.txt', '.pdf')
    os.rename(old_name, new_name)

# print new names
print('After rename')
print(os.listdir(folder))
