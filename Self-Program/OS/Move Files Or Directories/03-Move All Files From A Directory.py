import os
import shutil

source_folder = r"C:\Users\AliMT\Desktop\Self-Program\OS\Move Files Or Directories\source\\"
destination_folder = r"C:\Users\AliMT\Desktop\Self-Program\OS\Move Files Or Directories\destination\\"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)
