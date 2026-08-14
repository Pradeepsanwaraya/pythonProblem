# a=[1,2,3,4,5,6]
# for i in range(len(a)):
#     print(i,a[i])
# andismounttain

# a = [5, 10, 15]
# for i in range(len(a)):
#     print(a[i])

# a=[2,4,6]
# for i in range(len(a)):
#     print(i,a[i])

# a = [5, 10, 15, 20]
# sum=0
# for i in a:
#     sum=sum+i
# print(sum)

# a = [12, 5, 40, 9, 25]
# greater=0
# for i in a:
#     if i>greater:
#         greater=i
# print(greater)

# a = [2, 5, 8, 9, 10, 13]
# count=0
# for i in a:
#     if i%2==0:
#         count=count+1
# print(count)

# a = [10, 25, 18, 30, 15]

# Find=30
# for i in a:
#     if i==Find:
#         print("found")
#         break

# a = [10, 20, 30, 40, 50]
# f=30
# for i in range(len(a)):
#     if a[i]==f:
#         print(i)
#         break
# else:
#     print("not found")
# a = [10, 20, 30, 20, 40, 20, 50]
# count=0
# target = 20
# for i in range(len(a)):
#     if a[i]==target:
#         count=count+1
#         print(i)
# print("total count",count)


# a = [12, 5, 40, 9, 25]
# greater=a[0]
# index=0
# for i in range(len(a)):
#     if a[i]>greater:
#         greater=a[i]
#         index=i
# print(greater,index)
# a = [1, 2, 3]
# a.append(4)
# print(a)

# 📌 Interview Point
# append()
# Ek element add karta hai
# a.append([3,4]) → [1,2,[3,4]]	
# extend()
# List ke sabhi elements add karta hai
# a.extend([3,4]) → [1,2,3,4]

# Ye difference interview me bahut puchha jata hai.
# Topic: insert()

# append() hamesha last me add karta hai.

# insert() jis position par bolo, usi position par add karta hai.

# Example
# a = [10, 20, 30]

# a.insert(1, 100)

# print(a)

# Output:

# [10, 100, 20, 30]
# pop() element ko remove bhi karta hai aur return bhi karta hai.
# Example 1
# a = [10, 20, 30, 40]

# a.pop()

# print(a)

# count()
# a = [10, 20, 10, 30, 10]
# count=0
# for i in a:
#     count=count+1
# print(count)

