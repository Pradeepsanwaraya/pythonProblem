n=int(input("enter any number"))
sum=0
temp=n
while n>0:
    fact=1
    r=n%10
    for i in range(1,r+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if temp==sum:
    print("strong no")
else:
    print("not")



