import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.104.145",2323))
print("Connect \n")
data=s.recv(1024)
print(data.decode())
s.send("Hello I am Client".encode())
s.close()

