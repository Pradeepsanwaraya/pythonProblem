string=input("enter any string")
lower=''
for i in string:
    
    if i>='a' and i<='z':
        lower=lower+i
    elif i>='A' and i<='Z':
        r=ord(i)
        m=r+32
        lower=lower+chr(m)
print(lower)