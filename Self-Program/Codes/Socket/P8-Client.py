import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.100",1212))
print("Connected \n")
data=s.recv(1024)
print(data.decode())
s.close()
