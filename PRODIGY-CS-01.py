"""encrypting and decrypting text using ceaser cipher algorithm"""
import sys
def encrypt(name,keyvalue):
    for i in range(0,len(name)):
        if name[i]>="a" and name[i]<="z":
            name[i]=chr(ord(name[i])+keyvalue)
            if name[i]>"z":
                name[i]=chr(ord(name[i])-26)
        elif name[i]>="A" and name[i]<="Z":
            name[i]=chr(ord(name[i])+keyvalue)
            if name[i]>"Z":
                name[i]=chr(ord(name[i])-26)          
    return name
def decrypt(name,keyvalue):
    for i in range(0,len(name)):
        if name[i]>="a" and name[i]<="z":
            name[i]=chr(ord(name[i])-keyvalue)
            if name[i]<"a":
                name[i]=chr(ord(name[i])+26)
        elif name[i]>="A" and name[i]<="Z":
            name[i]=chr(ord(name[i])-keyvalue)
            if name[i]<"A":
                name[i]=chr(ord(name[i])+26)          
    return name

while(1):
    print("Enter your choice: 1) encrypt (e) 2) decrypt (d) 3)quit")
    m=input()
    if m=="e" or m=="E":
        name=list(input("Name: "))
        keyvalue=int(input("shift value: "))
        res=encrypt(name,keyvalue)
        print(''.join(res))
    elif m=="d" or m=="D":
        name=list(input("Name: "))
        keyvalue=int(input("shift value: "))
        res=decrypt(name,keyvalue)
        print(''.join(res))
    else:
        sys.exit()
    
