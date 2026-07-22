string=input("enter any string")

count=0
for i in string:
    if i>="A" and i<="Z":
        count=count+1
print(count)