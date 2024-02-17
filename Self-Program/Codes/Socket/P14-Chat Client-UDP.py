#UDP Client
from socket import *
s=socket (AF_INET,SCOK_DGRAM)
s.sendto("Hi ".encode(),("192.168.1.100",1212))
while True:
    data=s.recv(1024)
    print("recv=> "+data.decode())
    msg=input("You> ")
    s.sendto(msg.encode(),("192.168.1.100",1212))
s.close()
