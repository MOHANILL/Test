from socket import *
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s=socket(AF_INET,SOCK_STREAM)

ip=input("Enter ip :")
port=input("Enter port : ")
name=input("Enter name : ")

s.bind((ip,int(port)))
s.listen(5)

print("Server is Listenning ")

c,addr=s.accept()
print("connected to "+str(addr)+"\n")

while True:
    msg=input("-> ")
    c.sendall(name.encode()+"--> ".encode()+msg.encode())
    data=c.recv(1024)
    print(data.decode())
s.close()
