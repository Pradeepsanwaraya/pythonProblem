# Print Factors
# Count Factors
# Sum of Factors
# Prime Number
# Composite Number
# Perfect Number
# factor of a number
# num=int(input("enter any number"))
# i=1
# while i<=num:
#     if num%i==0:
#         print(i)
#     i=i+1

#count factor
# num=int(input("enter any number"))
# count=0
# i=1
# while i<=num:
#     if num%i==0:
#         count=count+1
#     i=i+1
# print(count)

#sum of factors
# num=int(input("enter any number"))
# Sum=0
# i=1
# while i<=num:
#     if num%i==0:
#         Sum=Sum+i
#     i=i+1
# print(Sum)

# Prime Number
num=int(input("enter any number"))
i=1
if num<2:
    print("not a prime number")
while i<=num//2:
    if num%i==0:
        print("not a pime")
        break
    i=i+1
else:
    print("prime number")