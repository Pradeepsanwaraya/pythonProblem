# Is base se ye questions banenge:
# ✅ Reverse Number
# Reverse + Palindrome
# Reverse + Difference
# Reverse + Sum
# Reverse + Product
# Mirror Difference
# Reverse Even Digits
# Reverse Odd Digits
# Reverse Count
# Reverse Compare

# n=int(input("enter any number"))
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# print(rev)


# n=int(input("enter any number"))
# rev=0
# temp=n
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if temp==rev:
#     print("palindrom")
# else:
#     print("not a palindrom")

# n=int(input("enter any number"))
# rev=0
# temp=n
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10

# deff=rev-temp
# print(deff)

# n=int(input("enter anym number"))
# rev=0
# sum=0
# while n>0:
#     r=n%20
#     rev=rev*10+r
#     sum=sum+r
#     n=n//10
# revs=rev+sum
# print(revs)

# n=int(input("enter anym number"))
# rev=0
# product=1
# while n>0:
#     r=n%20
#     rev=rev*10+r
#     product=product*r
#     n=n//10
# revs=rev+product
# print(revs)


# n=int(input("enter anym number"))
# rev=0
# product=0
# while n>0:
#     r=n%20
#     rev=rev*10+r
#     product=product*r
#     n=n//10
# revs=rev+product
# print(revs)

# | Question       | Change                            |
# | -------------- | --------------------------------- |
# | Reverse Number | `print(rev)`                      |
# | Palindrome     | `if rev == temp`                  |
# | Difference     | `diff = abs(temp - rev)`          |
# | Sum            | `sum = temp + rev`                |
# | Product        | `product = temp * rev`            |
# | Compare        | `if rev > temp`                   |
# | Count          | Reverse ke baad count             |
# | Mirror         | Reverse + Difference + Count + if |
