# num=int(input("enter any number"))
# i=1
# count=0
# while i<=num:
#     if num%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     print("prime")
# else:
#     print("not a prime")

    #nested for loop
n1=int(input("enter no1"))
n2=int(input("enter no2"))

while n1<=n2:
    j=1
    count=0
    while j<=n1:
        if n1%j==0:
            count=count+1
        j+=j
   
    if count==2:
        print(n1)
    n1=n1+1