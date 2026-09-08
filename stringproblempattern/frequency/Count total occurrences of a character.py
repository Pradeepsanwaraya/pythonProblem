s=input("enter a string")
target=input("enter a target")
count=0
for i in s:
    if i==target:
        count=count+1
print(count)