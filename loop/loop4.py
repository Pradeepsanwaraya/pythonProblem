num1=int(input("enter number 1 "))
num2=int(input("enter number 2 "))
while num1<num2:
    count=0
    j=1
    for j in range(1,num1+1):
        if num1%j==0:
            count=count+1
    if count==2:
        print(num1)
    num1=num1+1
        
  