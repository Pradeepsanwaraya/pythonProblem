string=input("enter any string")
count=0
for i in string:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        count=count+1
    elif i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1
print(count)
