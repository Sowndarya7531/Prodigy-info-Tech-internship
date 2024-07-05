"""password strength checker"""
def check_password_strength(password):
    length=1 if (len(password)>=8) else 0
    uppercase= 0
    lowercase=0
    digit=0
    specialcharacter=0
    count=0
    for i in password:
        if len(password)>=8:
            length=1
        if i.isupper():
            uppercase=1
        elif i.islower():
            lowercase=1
        elif i.isdigit():
            digit=1
        else:
            specialcharacter=1
    password_strength=[length,uppercase,lowercase,digit,specialcharacter]
    for i in range(0,len(password_strength)):
        if password_strength[i]==1:
            count+=1
    if all(password_strength):
        print("Strong Password")
    elif count>2 and count<=4:
        print("Moderate Password")
    else:
        print("weak")

if __name__=="__main__":
    password=input()
    check_password_strength(password)
