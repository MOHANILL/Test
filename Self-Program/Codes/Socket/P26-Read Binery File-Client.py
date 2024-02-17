import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect_ex(("192.168.1.50",8989))
print("Connected !")

while True:
    name=s.recv(1024)
    f=open(name,"rb")
    data=buffer(f.read())
    s.send(str(len(data)))
    print(s.recv(1024))

    s.sendall(data)
    f.close()
s.close()
