from socket import *
s=socket(2,1)

s.bind(("192.168.1.109",9999))
s.listen(5)

c,addr=s.accept()

f=open("C://new.txt","w")
data=c.recv(1024)
f.write(data.decode())

f.close()
s.close()

