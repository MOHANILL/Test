from socket import *
s=socket(2,1)
s.connect(("192.168.100",9999))
f=open("amt.txt","r")
data=f.read()
s.send(data.encode())

f.close()
s.close()

