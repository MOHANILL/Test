#UDP
from socket import *
s=socket(AF_INET,SOCK_DGRAM)#UDP Connection
s.bind(("192.168.204.231",1212))
print("Server Running on port 1212")
c,addr=s.recvfrom(1024)
print("Connected to "+str(addr)+"\n")
#print("Recived ="+str(c))
s.sendto("Hello I am server".encode(),addr)
s.close()
