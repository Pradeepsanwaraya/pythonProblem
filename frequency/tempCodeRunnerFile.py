n=int(input("enter any number"))
for i in range(10):
    count=0
    num=n
    while num>0:
        if num%10==i:
            count=count+1
        num=num//10
    print(i,count)
     

