num=int(input("enter any number"))
count=0
while num>0:
    if num%10!=0:
        count=count+1
    num=num//10
print(count)
