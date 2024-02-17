import glob
import os
import shutil

src_folder = r"C:\Users\AliMT\Desktop\Self-Program\OS\09-Move Files Or Directories\source\\"
dst_folder = r"C:\Users\AliMT\Desktop\Self-Program\OS\09-Move Files Or Directories\destination\\"

# move file whose name starts with string 'emp'
pattern = src_folder + "\emp*"
for file in glob.iglob(pattern, recursive=True):
    # extract file name form file path
    file_name = os.path.basename(file)
    shutil.move(file, dst_folder + file_name)
    print('Moved:', file)
