# n=int(input("enter any number"))
# smallest=9
# while n>0:
#     r=n%10
#     if smallest>r:
#         smallest=r
#     n=n//10
# print(smallest)

n=int(input("enter any number"))
l=0
while n>0:
    r=n%10
    if l<r:
        l=r
    n=n//10
print(l)