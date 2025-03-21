from collections import Counter

while True:
    files = []
    hashed = []
    
    nooffiles = int(input())
    if nooffiles == 0:
        break

    
    for _ in range(nooffiles):
        file = input()
        files.append(file)

    
    for f in files:
        xor = 0
        for y in f:
            xor = xor^ord(y) 
        hashed.append((xor))  

    collisions = 0

    for x in range(len(files)):
        for j in range(x+1, len(files)):
            if(files[x] == files[j]):
                continue
            elif(hashed[x] == hashed[j]):
                collisions = collisions + 1
    
    print(len(set(files)), collisions)

    


