import socket
while True:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    ip=input("IP : ")
    port=input("Port : ")
    r=s.connect_ex((ip,int(port)))

    if r==0:
        print("Open Port")
    else:
        print("Close Port")
s.close()
        
