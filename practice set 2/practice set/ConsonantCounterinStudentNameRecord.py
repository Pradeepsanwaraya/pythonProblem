string=input("enter any string")
count=0
for i in string:
    if i>='a' and i<='z':
        if i=='a' or i=='o' or i=='e' or i=='i' or i=='u':
            pass
        else:
            count=count+1
    elif i>='A' and i<='Z':
        
        if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            pass
        else:
            count=count+1
print(count)
