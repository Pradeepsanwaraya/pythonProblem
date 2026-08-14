n=int(input("enter a number"))
sq=n*n
sum=0
while sq>0:
    r=sq%10
    sum=sum+r
    sq=sq//10
if n==sum:
    print("neon no")
else:
    print("not")