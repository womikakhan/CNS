p = int(input("Enter the p value : "))
r = int(input("Enter the primitive root of p : "))

xa = int(input("Enter private key of A : "))
ya = int(pow(r,xa,p))
print("Public key of A is : ",ya)

xb = int(input("Enter private key of B : "))
yb = int(pow(r,xb,p))
print("Public key of B is : ",yb)

ka = int(pow(yb,xa,p))
kb = int(pow(ya,xb,p))

print()
print("Secret Key for A is : ",ka)
print("Secret Key for B is : ",kb)
