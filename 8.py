def gcd(k,t):
    while t!=0:
        c = k % t
        k = t
        t = c
    return k

d = 0
p = int(input("Enter the value of p : "))
q = int(input("Enter the value of q : "))
m = int(input("Enter the message : "))

n = p * q

totient = (p-1) * (q-1)

for e in range(2, totient):
    if(gcd(e,totient) == 1):
        break
    
for i in range(1,10):
    x = 1 + i * totient
    if x % e == 0:
        d = int(x/e)
        break
    
ct = int(pow(m,e,n))
dt = int(pow(ct,d,n))

print()
print("Text after encryption is : ",ct)
print("Text after decryption is : ",dt)
