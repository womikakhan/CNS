def encrypt(msg,key):
    res = ""
    for i in range(len(msg)):
        c = msg[i]
        if(c.isupper()):
            res += chr((ord(c) + n - 65) % 26 + 65)
        else:
            res += chr((ord(c) + n - 97) % 26 + 97)
            
    return res

def decrypt(msg,key):
    res = ""
    for i in range(len(msg)):
        d = msg[i]
        
        if(d.isupper()):
            res += chr((ord(d) - n - 65) % 26 + 65)
        else:
            res += chr((ord(d) - n - 97) % 26 + 97)
            
    return res

msg = input("Enter the Plaintext : ")
n = int(input("Enter the Key : "))

enc = encrypt(msg,n)
dec = decrypt(enc,n)

print("Message after encryption : ",enc)
print("Message after decryption : ",dec)
