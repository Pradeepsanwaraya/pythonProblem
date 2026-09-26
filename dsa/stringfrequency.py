s=input("enter a striing")
d={}
long=""
count=0
second=""
secondcount=0
for i in s:
    if i in d:
        d[i]+=1

    else:
        d[i]=1
for v,i in d.items():
    if i>count:
        secondcount=count
        second=long
        count=i
        long=v

    elif i>secondcount:
        secondcount=i
        second=v
print(second ,secondcount)
