n=int(input("enter any number"))
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("perfect no")
else:
    print("not a perfect no")