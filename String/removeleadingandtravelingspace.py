string=input("enter any string")
s=0
l=len(string)-1
for i in string:
    if string[s]==' ':
        s=s+1
    else:
        break
for i in string:
    if string[l]==' ':
        l=l-1
    else:
        break
for i in range(s,l+1):
    print(string[i],end=" ")
