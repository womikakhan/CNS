import sys
import string
import numpy as np
def findCipher(mat, key, n):
    
    cipherMatrix = []
    for i in range(n):
        sum1 = 0
        for j in range(n):
            
            sum1 += round(key[i][j]) * mat[j]

        cipherMatrix.append(sum1 % 26)
    
    return cipherMatrix

def validText(plainText, n):
    length = len(plainText) 
    if length % n != 0:
        
        rem = length % n
        numBef = length - rem
        numAfter = numBef + n
        
        for i in range(numAfter - length):
            plainText += 'x'
        
        
    return plainText
            

def encrypt():
    
    plainText = input("Enter the plaintext: ")
    
    plainText = plainText.lower()
    plainText = plainText.replace(" ","")
    n = int(input("Enter the key size: "))
    plainText = validText(plainText, n)
    
    key = list()
    
    for i in range(n):
        arr = list(map(int, input("Enter the {}th key row elements: ".format(i)).split()))
        key.append(arr)
    
    cipherText = ""
    
    letters = list(string.ascii_lowercase)
    
    for i in range(0,len(plainText),n):
        mat = []
        for j in range(i,n+i,1):
            mat.append(letters.index(plainText[j]))
        
        
        cipherMatrix = findCipher(mat, key, n)
        for k in range(n):
            cipherText += letters[cipherMatrix[k]]
    
    return cipherText
            

# for i in range(3):
#     arr = list(map(int, input().split()))
#     key.append(arr)


def decrypt():
    cipherText = input(("Enter the cipher text: "))
    cipherText = cipherText.replace(" ","")
    cipherText = cipherText.lower()
    
    n = int(input("Enter the key size: "))
    
    key = list()
    for i in range(n):
        arr = list(map(int, input("Enter the {}th key row elements: ".format(i)).split()))
        key.append(arr)

# for i in range(3):
#     arr = list(map(int, input().split()))
#     key.append(arr)


    plainText = ""
    key = np.array(key)
    key = key.astype(int)
    
    letters = list(string.ascii_lowercase)
    
    det = np.linalg.det(key)
    key = np.linalg.inv(key)

    for i in range(n):
        for j in range(n):
            key[i][j] = key[i][j]*det
            key[i][j] = key[i][j] % 26
            if key[i][j] < 0:
                key[i][j] += 26


    
    det %= 26
    if det < 0:
        det += 26
        
    multiply = 0
    for k in range(100):
        if round((k * det) % 26) == 1:
            multiply = k
            break
    
    for i in range(n):
        for j in range(n):
            key[i][j] = (key[i][j] * multiply) % 26
    
    for i in range(0,len(cipherText),n):
        mat = []
        for j in range(i,n+i,1):
            mat.append(letters.index(cipherText[j]))
        
        
        plainMatrix = findCipher(mat, key, n)
        for k in range(n):
            plainText += letters[plainMatrix[k]]
    
    return plainText

choice = 0

while True:
    
    choice = int(input())
    if choice == 0:
        cipherText = encrypt()
        print("Encrypted text is : {}".format(cipherText))
        print("Encrypted text is"+cipherText)


    elif choice == 1:
        plainText = decrypt()
        print("Decrypted text is : {}".format(plainText))
    else:
        sys.exit()
