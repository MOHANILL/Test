#UDP Server
from socket import *
s=socket(AF_INET,SOCK_DGRAM)
s.bind(("192.168.204.231",1212))
print("\nUDP CHAT Server Running On Port 1212 \n")
c,addr=s.recvfrom(1024)
while True:
    msg=input("You=> ")
    s.sendto(msg.encode(),addr)
    data=s.recv(1024)
    print("recv=> "+data.decode())
s.close()
