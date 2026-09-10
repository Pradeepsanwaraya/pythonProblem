l=list(map(int,input("enter a list").split()))
left=0
right=len(l)-1
target=20
while left<right:
    total=l[left]+l[right]
    if total==target:
        print(l[left]+l[right])
    elif target<total:
        left+=1
    else:
        right-=1
else:
    print("pair not fount")