s=input("enter a words").split()
done=""
for i in s:
    if i not in done:
        count=0
        for j in s:
            if i==j:
                count=count+1
        done=done+i
        print(count,i)
