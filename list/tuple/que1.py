# 1. Count Pairs with Difference K

# A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

# Problem Statement:

# Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

# Example:

# Input:

# N = 5





# K = 2
# ages[] = {1, 5, 3, 4, 2}

# Output:

# 3

# Explanation:

# (1,3), (3,5), (2,4)

arr=list(map(int,input("enter a list").split()))
target=int(input("enter a target"))
count=0
for i in range(len(arr)):
    for j in range(i+1):
        if abs(arr[i]-arr[j])==target:
            count=count+1
print(count)