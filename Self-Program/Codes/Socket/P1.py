import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("171.22.24.16",80))
print('Connected')
s.close()
