import os

file_path = r'C:\Users\AliMT\Desktop\Self-Program\OS\New folder\sample.txt'
# The default umask is 0o22 which turns off write permission of group and others
os.umask(0)
with open(os.open(file_path, os.O_CREAT | os.O_WRONLY, 0o777), 'w') as fh:
    fh.write('content')
