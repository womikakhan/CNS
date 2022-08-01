def keyGen(pt, key):
    key = list(key)
    
    if(len(pt) == key):
        return key
    else:
        for i in range(len(pt) - len(key)):
            key.append(key[i % len(key)])
            
    return ("".join(key))

def encrypt(pt, key):
    enc = []
    for i in range(len(pt)):
        x = (ord(pt[i]) + ord(key[i])) % 26
        x += ord('A')
        enc.append(chr(x))
    return("".join(enc))

def decrypt(ct, key):
    dec = []
    for i in range(len(ct)):
        x = (ord(ct[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        dec.append(chr(x))
    return("".join(dec))

pt = input("Enter the plaintext : ")
keyword = input("Enter the keyword : ")

key = keyGen(pt, keyword)

enc = encrypt(pt,key)
dec = decrypt(enc,key)

print("Encryption : ",enc)
print("Decryption : ",dec)
