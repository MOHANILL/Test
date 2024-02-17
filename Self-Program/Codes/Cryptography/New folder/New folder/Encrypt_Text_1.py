from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(key)

text = b"Salam Amir Reza"

f = Fernet(key)

Encrypt = f.encrypt(text)

print (Encrypt)


#key =b'0J_EIMQbLkTqau3TP-sHEHhA6d4shYeH6WpkqbEQ-ec='
#encrypt = b'gAAAAABkr9iTeiIG2gnMmRpLv9BvtGe_OVCK1SQ8BCki_TvBWMCwCNmxM_n5ClpuJYICmIsGtdkQZUbqJTPLrnMGtQJ_C7YqJA=='
