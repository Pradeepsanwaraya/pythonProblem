num=int(input("enter the number"))
Sum=0
temp=num
while num>0:
    r=num%10
    Sum=Sum*10+r
    num=num//10
print("reverse",Sum)
if temp==Sum:
    print("palindrome")
else:
    
    
    nextpalin=temp+1
    while True:
        num1=nextpalin
        rev=0
        while num1>0:
            m=num1%10
            rev=rev*10+m
            num1=num1//10
        if nextpalin==rev:
            print(rev)
            break
        nextpalin=nextpalin+1





    