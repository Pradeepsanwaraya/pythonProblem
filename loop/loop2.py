num=int(input("enter the number"))
Sum=0
count=0
product=1
temp=num
while num>0:
    r=num%10
    Sum=Sum+r
    product=product*r
    
    num=num//10

print(Sum)
print(product)
while temp>0:
    r=temp%10
    count=count+1
    temp=temp//10
print(count)