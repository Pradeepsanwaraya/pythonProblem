# Level 1 (10 Programs)
# Print 1 to 10
# Print 10 to 1
# Print 1 to N
# Print N to 1
# Print Even Numbers
# Print Odd Numbers
# Sum of 1 to N
# Product of 1 to N
# Table of a Number
# Count Numbers
for i in range(1,10+1):
    print(i)
for i in range(10,1,-1):
    print(i)
num=int(input("enter any number"))
for i in range(1,num+1):
    print(i)
for i in range(num,0,-1):
    print(i)
for i in range(1,num+1):
    if i%2==0:
        print(i)
for i in range(1,num+1):
    if i%2!=0:
        print(i)
sum=0
product=0
for i in range(1,num+1):
    sum=sum+i
    product=product*i
print("sum of numbers=",sum,"product of number=",product)
table=15
for i in range(1,10+1):
    
    print(table,"x",i,"=",table*i)
count=0
for i in range(1,num+1):
    count=count+1
print(count)