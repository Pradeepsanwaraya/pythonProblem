# Sum & Number Logic
# Sum of first n natural numbers
# Sum of even numbers
# Sum of odd numbers
# Product of first n numbers
# Factorial
# Sum of digits
# Product of digits
# Reverse a number
# Count digits
# Largest digit
# Smallest digit
# Average of digits
# Sum of squares
# Sum of cubes
# Sum of first n natural numbers
# n=int(input("enter any number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)
# sum of even number
# n=int(input("enter any number"))
# sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         sum=sum+i

# print(sum)
# n=int(input("enter any number"))
# sum=0
# for i in range(1,n+1):
#     if i%2!=0:
#         sum=sum+i
# print(sum)
# Product of first n numbers
# n=int(input("enter any number"))
# product=1
# for i in range(1,n+1):
#     product=product*i
# print(product)
# Factorial
# n=int(input("enter any number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
# Sum of digits
# n=int(input("enter any number"))
# sum=0
# while n>0:
#     r=n%10
#     sum=sum+r
#     n=n//10
# print(sum)
# Largest digit
# n=int(input("enter any number"))
# large=0
# while n>0:
#     r=n%10
#     if r>large:
#         large=r
#     n=n//10
# print(large)
# n=input("enter any number")
# small=9
# for i in n:
#     digit=int(i)
#     if digit<small:
#         small=digit
# print(small)
# Average of digits
# n=int(input("enter any number"))
# c=0
# s=0
# while n>0:
#     r=n%10
#     s=s+r     
#     c=c+1
#     n=n//10
# avg=s/c
# # print(avg)
# n1=int(input("enter any number"))
# n2=int(input("enter any number"))
# for i in range(n1,n2):
#     sum=0
#     num=i
#     square=0
#     while num>0:

#         r=num%10
#         square=r*r
#         sum=sum+square
#         num=num//10
#     print(sum)
# n1=int(input("enter any number"))
# n2=int(input("enter any number"))
# for i in range(n1,n2+1):
#     sum=0
#     num=i
#     cube=1
#     while num>0:
#         r=num%10
#         cube=r*r*r
#         sum=sum+cube
#         num=num//10
#     print(sum)
# n=int(input("enter any number"))
# fre=0
# while n>0:
#     r=n%10
#     if r!=fre:
#         sum=r
#     n=n//10
#     fre=fre+r
# print(sum)
#  Sum of first n natural numbers
# n=int(input("enter your number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)
# s=input("enter a ctring")
# d=input("frequency")
# count=0
# for i in s:
#     if i==d:
#         count=count+1
# print(count)
# s=input("enter a string")
# done=''
# maxcount=0
# maxch=''
# for i in s:
#     count=0
#     if i not in done:
#         for j in s:
#             if i==j:
#                 count=count+1
#         if count>maxcount:
#             maxcount=count
#             maxch=i
            
#         done=done+i
# print(maxch,maxcount)
# n=int(input("enter any string"))
# maxcount=0
# digit=0
# for i in range(10):
#     count=0
#     num=n
#     larger=0
#     while num>0:
#         if num%10==i:
#             count=count+1
#         num=num//10
#     if count>maxcount:
#         maxcount=count
#         digit=i
# print(digit,maxcount)

# 1. Frequency
# if count > 0:
#     print(i, count)
# 2. Repeated Digits
# if count > 1:
#     print(i)
# 3. Unique Digits
# if count == 1:
#     print(i)
# 4. Total Repeated Digits

# Pehle loop ke upar:

# total = 0

# Loop ke andar:

# if count > 1:
#     total += 1

# Loop ke baad:

# print(total)
# 5. Total Unique Digits

# Pehle:

# total = 0

# Loop ke andar:

# if count == 1:
#     total += 1

# Baad me:

# print(total)
# 6. Maximum Frequency Digit

# Loop ke upar:

# maxcount = 0
# maxdigit = 0

# Loop ke andar:

# if count > maxcount:
#     maxcount = count
#     maxdigit = i

# Baad me:

# print(maxdigit, maxcount)
# 7. First Repeated Digit

# Loop ke andar:

# if count > 1:
#     print(i)
#     break
# 8. First Unique Digit

# Loop ke andar:

# if count == 1:
#     print(i)
#     break
# 🔥 Pattern yaad rakh

# Base code = Same

# Sirf ye condition badlegi:

# if count > 0:

# ya

# if count > 1:

# ya

# if count == 1:

# ya

# if count > maxcount: