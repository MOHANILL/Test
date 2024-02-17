#session 8
pip install pytest-shutil
import os
import shutil
source_folder=r'D:\python learn\BP\sor'
destination_folder=r"D:\python learn\BP\des"
#fetch all files
for file_name in os.listdir(source_folder):
    #construct full file path
    source=source_folder+file_name
    destination=destination_folder+file_name
    #move only files

    shutil.move(source, destination)
    print('Moved:', file_name)
