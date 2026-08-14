n=int(input("enter any number"))
l=len(str(n))
rev=0
temp=n
while n>0:
    r=n%10
    rev=rev+r**l
    n=n//10
if temp==rev:
    print("armstorm")

else:
    print("not a armstrom no")
