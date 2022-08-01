import string

def key_matrix_generation(key):
    
    atoz=string.ascii_lowercase.replace('j','.')
    
    #print("\n"+atoz)
    
    Key_matrix = [ '' for i in range(5)] #list comprehension
    
    i = 0 #row
    j = 0 #col
    
    for c in key:
        if c in atoz:  #not being used before
            Key_matrix[i] += c #add the character to it
            
            
            atoz = atoz.replace(c, '.') #no character should repeat
            
            j += 1 #increment column
            if j > 4: 
                i += 1 #incr row
                j = 0  #set col to 0
                
    for c in atoz:
        if c !='.':
            Key_matrix[i] += c
            
            j += 1
            if j > 4:
                i += 1
                j = 0
    return Key_matrix

key=input("Enter the key : ")
key=key.lower()

key_matrix = key_matrix_generation(key)

print(key_matrix)

#Rule 1

p=input("Enter the plaintext : ")

p=p.lower()
 
pt=[]
ct=[]

i = 0

while i < len(p):
    a=p[i]
    b=''
    
    if (i + 1) == len(p):
        b='x'
    else:
        b = p[i+1]
        
    if a!=b:
        pt.append(a + b)
        i += 2
    else:
        pt.append(a + 'x')
        i += 1
        
print(pt)

#Rule 2

for pair in pt:
    applied = False
    
    for row in key_matrix:
        if pair[0] in row and pair[1] in row:
            
            j0 = row.find(pair[0])
            j1 = row.find(pair[1])
            
            c = row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
            ct.append(c)
            applied = True
            
    if applied:
        continue
#Rule 3
    for j in range(5):
        col="".join([key_matrix[i][j] for i in range(5)]) 
        
        if pair[0] in col and pair[1] in col:
            
            i0 = col.find(pair[0])
            i1 = col.find(pair[1])
            
            c = col[(i0 + 1) % 5] +col[(i1 + 1) % 5]
            
            ct.append(c)
            
            applied = True
    if applied:
        continue
    
#Rule 4
    i0 = 0
    i1 = 0
    j0 = 0
    j1 = 0
    
    for i in range(5):
        row = key_matrix[i]
        
        if pair[0] in row:
            i0 = i
            j0 = row.find(pair[0])
            
        if pair[1] in row:
            i1 = i
            j1 = row.find(pair[1])
            
    c = key_matrix[i0][j1] + key_matrix[i1][j0]
        
    ct.append(c)
        
print(ct)
