from cryptography.fernet import Fernet

key = b'rBrg0XuAaV348ssUUR-1gJtwjsrA1ZYNSm7H9bPAlco='


file = open("new_1.jpg","rb")

data = file.read()

file.close()

#print data

New_File = open("1.jpg","wb")

f = Fernet(key)

Decrypt = f.decrypt(data)

New_File.write(Decrypt)

New_File.close()



