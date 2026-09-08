s=input("enter a string")
done=""
for i in s:
    if i not in done:    
        count=0
        for j in s:
            if i==j:
                count=count+1
        done=done+i
        if count>0:
            print(count,i)