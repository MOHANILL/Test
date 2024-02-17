"""
With the help of the rename() method we can rename a file and then move it to a new location as well.
This is done by passing the new location to the rename() method’s dst parameter.

Consider the below example where we are defining two different folders as the source and destination separately.
Then using the rename() method, we are changing the name and the location of the file.

Finally when we print the files in the new location we can see the file in the list.
"""
import glob
import os

# Old and new folder locations
old_folder = r"E:\ParentFolder\SubFolder\\"
new_folder = r"E:\ParentFolder\New_location\\"

# Old and new file names
old_name = old_folder + "a.txt"
new_name = new_folder + "a_new.txt"

# Moving the file to the another location

os.rename(old_name, new_name)
