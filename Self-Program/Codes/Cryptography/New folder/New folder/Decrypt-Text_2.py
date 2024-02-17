from cryptography.fernet import Fernet


key = b'0J_EIMQbLkTqau3TP-sHEHhA6d4shYeH6WpkqbEQ-ec='

Encrypt = b'gAAAAABkr9iTeiIG2gnMmRpLv9BvtGe_OVCK1SQ8BCki_TvBWMCwCNmxM_n5ClpuJYICmIsGtdkQZUbqJTPLrnMGtQJ_C7YqJA=='

f = Fernet(key)

Decrypt = f.decrypt(Encrypt)

print (Decrypt)
