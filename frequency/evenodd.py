num=int(input("enter any number"))
odd=0
count=0
while num>0:
    r=num%10
    if r%2==0:
        count=count+1
    else:
        odd=odd+1

    num=num//10

print(count,odd)