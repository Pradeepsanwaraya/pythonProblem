n=int(input("enter any number"))
sq=n*n
while n>0:
    r=n%10
    sq2=r*r
    break
if n==sq2:
    print("automorphic")
else:
    print("not a")
    