# 1 3 5 8 12 15
l=list(map(int,input("enter a list").split()))
left=0
target=7
right=1
while left<len(l)-1:
    diff=l[right]-l[left]
    if diff==target:
        print(l[left],l[right])
    elif target<diff:
        left+=1
    else:
        right+=1
else:
    print("pair not")