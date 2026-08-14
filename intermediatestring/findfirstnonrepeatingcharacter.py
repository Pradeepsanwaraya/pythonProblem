string=input("enter any string")

done=''
for i in string:
    if i not in done:
        count=0
        for j in string:
            if j==i:
                count=count+1
                print(i,count)
        done=done+i
if count==1:
    print(i)
else:
    print("there is no repeating character")