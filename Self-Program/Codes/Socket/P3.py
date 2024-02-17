import socket
while True:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    ip=input("IP : ")
    port=input("PORT : ")

    try:
        s.connect((ip,int(port)))
        print("Open Port")
    except:
        print("Close Port")
        
