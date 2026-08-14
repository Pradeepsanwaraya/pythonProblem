# 2.
# Secure Password Analysis

# A cybersecurity team wants to identify pairs of passwords having no common characters.

# Problem Statement:

# Given N strings, count the number of pairs that do not share any common character.

# Example:

# Input

# N = 4
# passwords[] = {"abc", "de", "fg", "ad"}

# Output

# 3

# Explanation

# ("abc","de")
# ("abc","fg")
# ("de","fg")
n=int(input("enter a number"))
arr=[]
for i in range(n):
    x=input("enter a n arry of string")
    arr.append(x)
tp=tuple(arr)
print(tp)
count=0
for i in range(n):
    for j in range(i + 1, n):
        common = False
        for a in tp[i]:
            for b in tp[j]:
                if a==b:
                    common=True
        if common==False:
            count=count+1
print(count)