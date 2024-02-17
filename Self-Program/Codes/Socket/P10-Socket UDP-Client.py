from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s.sendto("Hello I am client ".encode(),("192.168.204.231",1212))
data=s.recv(1024)
print(data.decode())
s.close()
