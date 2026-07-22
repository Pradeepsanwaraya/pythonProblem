string=input("enter any string")
upper=''
for i in string:
    
    if i>='A' and i<='Z':
        upper=upper+i
    
    elif i>='a' and i<='z':
        r=ord(i)
        m=r-32
        upper=upper+chr(m)

print(upper)


