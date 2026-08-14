string=input("enter any number")
done=''
for i in string:
    if i not in done:
        count=0
        for j in string:
            if i!=j:
                count=count+1
        done=done+i
    if count>0:
        print(i)
        break


s=input("enter any string")
new='' 
for i in s:
    if i not in new:
        new=new+i
print(new)