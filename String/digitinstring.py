string=input("enter any string")
count=0
for i in string:
    if i>='0' and i<='9':
        count=count+1
print(count)