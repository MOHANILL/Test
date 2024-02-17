import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("171.22.124.16",80))
print("Connected")
s.send("GET /index.php HTTP/1.0 \n\n".encode())
data=s.recv(1024)
print(data.decode())
s.close()
