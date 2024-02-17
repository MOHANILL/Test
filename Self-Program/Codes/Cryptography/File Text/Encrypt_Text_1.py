from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

text = b"Hello Shyda , how are you ?"

f = Fernet(key)

Encrypt = f.encrypt(text)

print (Encrypt)


#key =b'sSK27FcL1bcKEoxnLvaV0uZlPLS0g2Cp1vaNE6zF9U4='
#encrypt =b'gAAAAABkT92rKREgcOz4HaDp7ECgdD5uX14MUsNI6jyiViXfcxy-KKGBPWgtW02WZwp318n2paPjLM6eG3s9vIQhP3VBsZUBwA=='
