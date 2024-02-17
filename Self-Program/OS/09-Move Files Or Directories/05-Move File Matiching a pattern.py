import glob
import os
import shutil

src_folder=r'C:\Users\AliMT\Desktop\Self-Program\OS\09-Move Files Or Directories\source\\'
dst_folder=r'C:\Users\AliMT\Desktop\Self-Program\OS\09-Move Files Or Directories\destination\\'

#Sreatch files with .txt extention in source directory
pattern="\*.jpg"
files=glob.glob(src_folder+pattern)

#move the files with txt destination
for file in files:
    file_name=os.path.basename(file)
    shutil.move=(src_folder+file_name)
    print('Moved :',file)
