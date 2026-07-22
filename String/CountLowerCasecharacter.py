string=input("enter any string")
count=0
for i in string:
    if i>='a' and i<='z':
        count=count+1
print(count)