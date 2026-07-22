# num=int(input("enter any number"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+1
# if count==2:
#     print("prime number ")
# else:
#     print("not a prime number")
# # next prime 
# num=int(input("enter any number"))
# while True:
#     num=num+1
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     if count==2:
#         print("next prime=",num)
#         break
#previous prime
# num=int(input("enter any number"))
# while True:
#     num=num-1
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     if count==2:
#         print("previous prime",num)
#         break
#composite number
# num=int(input("enter any number"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+1

# if count>2:
#     print("composite number ")
# else:
#     print("not  A composite number")
# prime number next prime immmediate prime
# num=int(input("enter any number"))
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+1
# if count==2:
#     print("prime number")
#     nextp=num
#     while True:
#         nextp=nextp+1
#         count=0
#         for i in range(1,num+1):
#             if num%i==0:
#                 count=count+1
#         if count==2:
#             print("next prime=",nextp)
#             break
# else:
#     print("not a prime number")
#     while True:
#         num=num-1
#         count=0
#         for i in range(1,num+1):
#             if num%i==0:
#                 count=count+1
#         if count==2:
#             print("previous prime =", num)
#             break
# #next prime and difference
# num=int(input("enter any number"))
# temp=num
# while True:
#     num=num+1
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count=count+1
#     gap=num-temp
#     if count==2:
#         print("next prime=",num)
#         print("difference =",gap)
#         break
# - Check Composite or Not
# - Count total factors
# - Print smallest factor other than 1
# num=int(input("enter any number"))
# count=0
# temp=num
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+1
# if count>2:
#     print("composite number")
#     res=0
#     st=True
#     for i in range(1, num+1):
#         if num%i==0:
#             res=res+1
#             if  i>1 and st == True:
#               print(f"smallest factor other than 1 :- {i}")
#               st=False
             
    
#     print(res)



# 10.Zero Count Prime Scanner

# A banking system checks account numbers.

# Write a program to:

# - Count zero digits
# - Find sum of digits
# - Add zero count and sum
# - Multiply by smallest digit
# - Check whether final result is Prime or Not

# Input:
# 908406

# Output:
# Zero Count = 2
# Sum = 27
# Smallest Digit = 0
# Final Result = 0
# Not Prime

n = int(input("Enter the number :-"))
zcount=0
sum=0
sdig=9

while n :
    dig = n%10
    if dig == 0:
          zcount+=1
    sum+=dig 
    if dig<sdig:
          sdig=dig
    n=n//10
print("zero count",zcount)
print("sum",sum)
print("sdigit",sdig)
final_num =(zcount+sum)*sdig
i=2
if final_num<2:
    print("Given number is not prime")
else:
    while i<=final_num//2:
        if final_num%i==0:
              print(f"Given number is not prime number :..")
              break
    else:
        print("Given number is prime number ")





     
    
     
