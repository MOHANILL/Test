from cryptography.fernet import Fernet


key = b'k77ZV1kMysuWRvYHjOe6GU4qCJ9T8OrmWijP-hlISQI=' 

Encrypt = b'gAAAAABktlrUK09Hp5t_2ZGxdS88WOUjldTJMlq6TIn-lwwlKTGAOEnB8wlGcUQKOayRCDRb1Srw5nwFdGBI0-PsJp8mAJWYLjjCdhFiaa0t-Sw2SBncuss='

f = Fernet(key)

Decrypt = f.decrypt(Encrypt)

print (Decrypt)
