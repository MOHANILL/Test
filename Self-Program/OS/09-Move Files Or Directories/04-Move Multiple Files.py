import shutil
import os

source_folder = r"C:\Users\AliMT\Desktop\Self-Program\OS\09-Move Files Or Directories\source\\"
destination_folder = r"C:\Users\AliMT\Desktop\Self-Program\OS\09-Move Files Or Directories\destination\\"
files_to_move = ['a.txt', 'b.jpg']

# iterate files
for file in files_to_move:
    # construct full file path
    source = source_folder + file
    destination = destination_folder + file
    # move file
    shutil.move(source, destination)
    print('Moved:', file)
