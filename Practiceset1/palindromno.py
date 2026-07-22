# num=int(input("enter any number"))
# temp=num
# sum=0
# while num>0:
#     r=num%10
#     sum=sum*10+r
#     num=num//10
# if temp==sum:
#     print("palindrom")
# else:
#     print("not a palindrom")
#palindrom no to the given range
num1=int(input("enter no 1 "))
num2=int(input("enter no 2 "))
while num1<=num2:
    sum=0
    temp=num1
    num=num1
    while temp>0:
        r=temp%10
        sum=sum*10+r
        temp=temp//10
    if temp==sum:
        print(temp)
    num1=num1+1