# Level 2 – Part A
# Count Digits
# Sum of Digits
# Product of Digits
# Reverse Number
# First Digit
# Last Digit
# Largest Digit
# Smallest Digit
# Count Even Digits
# Count Odd Digits

# Count Digits
num=int(input("enter num"))
count=0
while num>0:
    
    count=count+1
    num=num//10 
print(count)

# Sum of Digits

# num=int(input("enter any number"))
# som=0
# while num>0:
#     r=num%10
#     som=som+r
#     num=num//10
# print(som)

# Product of Digits

# num=int(input("enter any number"))
# product=1
# while num>0:
#     r=num%10
#     product=product*r
#     num=num//10
# print(product)


# num=int(input("enter any number"))
# rev=0
# while num>0:
#     r=num%10
#     rev=rev*10+r
#     num=num//10
# print(rev)

#  First Digit

# num=int(input("enter any number"))
# rev=0
# while num>0:
#     r=num%10
#     rev=rev*10+r
#     num=num//10
# f=rev%10
# print(f)
#last digit
# num=int(input("enter any number"))
# rev=0
# while num>0:
#     l=num%10
#     break
# print(l)
#Largest Digit
# num=int(input("enter any number"))
# lastdigit=1
# while num>0:
#     r=num%10
#     if lastdigit<r:
#         lastdigit=r
#     num=num//10
# print("largest is = ", lastdigit)
# #smallest digit
# num=int(input("enter any number"))
# smallest=9
# while num>0:
#     r=num%10
#     if smallest>r:#456 6 
#         smallest=r
#     num=num//10
# print("smallest is =", smallest)

#even digit in a number
# num=int(input("enter any number "))
# count=0
# while num>0:
#     r=num%10
#     if r%2==0:
#         count=count+1
#     num=num//10
# print("even digit is =", count)

#count odd digit in a number
# num=int(input("enter any number "))
# count=0
# while num>0:
#     r=num%10
#     if r%2!=0:
#         count=count+1
#     num=num//10
# print("odd digit is =", count)