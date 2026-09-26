l=list(input("enter a list of words").split())
d={}
count=0
long=""
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i,v in d.items():
    if v>count:
        count=v
        long=i
print(long,count)