string=input("enter any string")
toggle=''
for i in string:
    if i>='a' and i<='z':
        r=ord(i)
        m=r-32
        toggle=toggle+chr(m)


    elif i>='A' and i<='Z':
        u=ord(i)
        n=u+32
        toggle=toggle+chr(n)

print(toggle)