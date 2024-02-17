import socket
from datetime import *

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.204.231",1212))
s.listen(5)
while True:
    session,addr=s.accept()
    
    print("connected to " +str(addr)+"\n")
    today=date.today()
    session.sendall("today's date:".encode()+str(today).encode())
s.close()
