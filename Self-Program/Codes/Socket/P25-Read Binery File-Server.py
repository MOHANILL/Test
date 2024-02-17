import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.1.100",8989))
s.listen(5)
print("Connected to Port ")

while True:
    c,adder=s.accept()
    print("Connect to "+str(adder)+"\n")
    name=input("Enter Your File Name :")
    c.sendall(name.encode())
    
    f=open("E:\\Python Projects\\Modules\\Socket"+name,"wb")
    data1=c.recv(c.recv(1024))
    c.sendall("Resive Lenght Data".encode())
    
    my_write=str(c.recv(int(data1))) 
    f.write(my_write.encode())
    print("finish")
    f.close()
s.close()
c.close()