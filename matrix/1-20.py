# Print all elements
# Print even elements
# Print odd elements
# Count even elements
# Count odd elements
# Sum of all elements
# Product of all elements
# Find maximum
# Find minimum
# Count positive numbers
# Count negative numbers
# Count zeros
# Sum of positive numbers
# Sum of negative numbers
# Print elements greater than K
w
# Count elements greater than K
# Count elements smaller than K
# Find first even number
# Find first negative number

# Print all elements
# l=list(map(int,input("enter  a list").split()))
# for i in range(len(l)):
#     print(l[i],end=" ")
# n=int(input("enter a number"))
# l=[]

# Print even elements
# for i in range(n):
#     x=int(input("enter a list element"))
#     l.append(x)
# for i in range(len(l)):
#     if l[i]%2==0:
#         print(l[i],end=" ")

# Print odd elements
# n=int(input("enter a number"))
# l=[]
# for i in range(n):
#     x=int(input("enter a list element"))
#     l.append(x)
# for i in range(len(l)):
#     if l[i]%2!=0:
#         print(l[i],end=" ")

# Count even elements
# n=int(input("enter number of element"))
# l=[]
# for i in range(n):
#     x=int(input("enter element of list"))
#     l.append(x)
# count=0
# for i in range(len(l)):
#     if l[i]%2==0:
#         count=count+1
# print(count)

# Count odd elements
# n=int(input("enter a number"))
# l=[]
# for i in range(n):
#     x=int(input("enter element of list "))
#     l.append(x)
# count=0

# for i in range(len(l)):
#     if l[i]%2==0:
#         count=count+1
# print(count)

# Sum of all elements
# n=int(input("enter a number"))
# l=[]
# for i in range(n):
#     x=int(input("entyer  a element of list"))
#     l.append(x)
# sum=0
# for i in range(len(l)):
#     sum=sum+l[i]
# print(sum)

# Product of all elements
# n=int(input("enter a number"))
# l=[]
# for i in range(n):
#     x=int(input("enter a element of list"))
#     l.append(x)
# product=1
# for i in range(len(l)):
#     product=product*l[i]
# print(product)


# Find maximum

# n=int(input("enter a number of elements in a list"))
# l=[]
# for i in range(n):
#     x=int(input("enter a list element"))
#     l.append(x)
# maxi=l[0]
# for i in range(len(l)):
#     if l[i]>maxi:
#         maxi=l[i]
# print(maxi)
#find minimum
# n=int(input("enter a number of list elemnet"))
# l=[]
# for i in range(n):
#     x=int(input("enter element of list"))
#     l.append(x)
# mini=l[0]
# for i in range(len(l)):
#     if l[i]<mini:
#         mini=l[i]
# print(mini)
# Count positive numbers
# n=int(input("enter a number of list elements"))
# l=[]
# for i in range(n):
#     x=int(input("enter a list element"))
#     l.append(x)
# for i in range(len(l)):
#     if l[i]>=0:
#         print(l[i],end=" ")

# Count negative numbers
# n=int(input("enter a number"))
# l=[]
# for i in range(n):
#     x=int(input("enter a list element"))
#     l.append(x)
# for i in range(len(l)):
#     if l[i]<0:
#         print(l[i],end=" ")

#count Zero
# n=int(input("enter a number "))
# l=[]
# for i in range(n):
#     x=int(input("enter elements of list"))
#     l.append(x)
# count=0
# for i in range(len(l)):
#     if l[i]==0:
#         count=count+1
# print(count)

# # Sum of positive numbers
# n=int(input("enter  a number"))
# l=[]
# for i in range(n):
#     x=int(input("enter a list element"))
#     l.append(x)
# sum=0
# for i in range(len(l)):
#     if l[i]>=0:
#         sum=sum+l[i]
# print(sum)

# Sum of negative numbers

# n=int(input("enter a number of list"))
# l=[]
# for i in range(n):
#     x=int(input("enter a element of list"))
#     l.append(x)
# sum=0
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]<0:
#             sum=sum+l[i]
# print(sum)


# Print elements greater than K
# n=int(input("enter a list number"))
# l=[]
# for i in range(n):
#     x=int(input("enter a number"))
#     l.append(x)
# k=int(input("enter a target number"))
# N=[]
# for i in range(len(l)):
#         if l[i]>k:
#             N.append(l[i])
# print(N)