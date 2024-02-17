import socket
import pyaes

key="key_is_python_AH"

aes=pyaes.AESModeOfOperationCTR(key)
plain_text=b"this is golden"
cipher_text=aes.encrypt(plain_text)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.1.100",444))

print(aes.decrypt(s.recv(1024)))

s.close()
