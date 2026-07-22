string=input("enter any string")
count=0
for i in string:
    if i>='0' and i<='9':
        pass
    elif i>='a' and i<='z':
        pass
    elif i>='A' and i<='Z':
        pass
    else:
        count=count+1
print(count)