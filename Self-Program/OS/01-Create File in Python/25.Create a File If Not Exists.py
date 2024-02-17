import os

file_path = r'E:\Golrang\Code\profit.txt'
if os.path.exists(file_path):
    print('file already exists')
else:
    # create a file
    with open(file_path, 'w') as fp:
        # uncomment if you want empty file
        fp.write('This is first line')
