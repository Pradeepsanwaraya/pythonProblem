l=list(map(int,input("enter a element of list").split()))
d={}

for i in range(len(l)):
    if l[i] not in d:
        d[l[i]]=1
    else:
         d[l[i]]=d[l[i]]+1
print(d)