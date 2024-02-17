import pyaes
import socket

key= "key_is_python_AH"
aes = pyaes.AESModeOfOperationCTR(key)
plain_text=b"this is golden"
cipher_text=aes.encrypt(plain_text)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.1.9",5555))
s.listen(5)
while True:
    c,addr=s.accept()
    c.sendall(cipher_text)
    print(cipher_text)
s.close()
c.close()
