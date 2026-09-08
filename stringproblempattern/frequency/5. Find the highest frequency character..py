s=input("enter a character")
done=""
maxi=0
mxch=""
for i in s:
    if i not in done:
        count=0
        for j in s :
            if i==j:
                count=count+1
        done=done+i
        if count>maxi:
            maxi=count
            mxch=i
print(maxi,mxch)