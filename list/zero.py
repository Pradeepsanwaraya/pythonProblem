arr = [0, 1, 0, 3, 12]
left = 0
right = 0
while right < len(arr):
    if arr[right]!=0:
        temp=arr[left]   
        arr[left]=arr[right]
        arr[right]=temp
        left+=1
    right+=1
print(arr)