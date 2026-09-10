l=list(map(int,input("enter a list").split()))
target=8
left=0
right=len(l)-1
while left<right:
    total=l[left]+l[right]
    if total==target:
        print(l[left],l[right])
    elif total>target:
        right-=1
    else:
        left+=1