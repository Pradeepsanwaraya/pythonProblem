arr=list(map(int,input("enter a list").split()))
n=len(arr)
peak=-1
for i in range(n):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
            peak=i
            break
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            peak=i
            break
    else:
        if arr[i]>=arr[i+1] and arr[i]>=arr[i-1]:
            peak=i
            break
if peak!=-1:
    print(peak)
else:
    ("no peak found")
