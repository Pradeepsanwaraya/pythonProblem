# # row=int(input("enter a row"))
# # col=int(input("enter a column"))
# # A=[]
# # for i in range(row):
# #     temp=[]
# #     for j in range(col):
# #         x=int(input("enter a list"))
# #         temp.append(x)
# #     A.append(temp)

# # row=int(input("enter a row"))
# # col=int(input("enter a column"))
# # B=[]
# # for i in range(row):
# #     temp=[]
# #     for j in range(col):
# #         x=int(input("enter a list"))
# #         temp.append(x)
# #     B.append(temp)
# # print(B)
# # res=[]
# # for i in range(row):
# #     trep=[]
# #     for j in range(col):
# #         trep.append(A[i][j]+B[i][j])
# #     res.append(trep)
# # print(res)
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
# row=int(input("enter a row"))
# target=2
# A=[]
# for j in range(row):
#     x=int(input("enter a list"))
#     A.append(x)
# print(A)


# A=list(map(int,input("enter a list").split()))
# target=2
# count=0
# for i in range(len(A)):
#     # count=0
#     for j in range(i+1,len(A)-1):
#         if A[i]-A[j]==target:
#            count=count+1
# print(count)


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


# 3.

# MATRIX PERFORMANCE EVALUATION SYSTEM

# A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

# The HR department wants a menu-driven application to analyze employee performance.

# Menu
# 1. Find Employee with Highest Total Score
# 2. Find Month with Lowest Average Score
# 3. Display Employee-wise Maximum Score
# 4. Exit
# Requirements
# Choice 1 – Find Employee with Highest Total Score
# Calculate the sum of each row.
# Display the employee number having the highest total score.
# Choice 2 – Find Month with Lowest Average Score
# Calculate the average of each column.
# Display the month having the lowest average score.
# Choice 3 – Display Employee-wise Maximum Score
# Find and display the maximum value present in each row.
# Sample Input
# 10 20 30
# 40 50 60
# 25 35 45
# Output
# Employee 2 has Highest Total Score = 150

# Month 1 Average = 25
# Month 2 Average = 35
# Month 3 Average = 45

# Employee 1 Max Score = 30
# Employee 2 Max Score = 60
# Employee 3 Max Score = 45


# 4.
# Find common elements in three sorted arrays.
# Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
# Note: can you take care of the duplicates without using any additional Data Structure?
# Example 1:
# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.


# 5.

# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers.
# Your task is to create an array of alternate positive and negative numbers
# without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.

# Example 1:
# Input:
# N = 9
# Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
# Output:
# 9 -2 4 -1 5 -5 0 -3 2
# Example 2:
# Input:
# N = 10
# Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output:
# 5 -5 2 -2 4 -8 7 1 8 0



# r=int(input("enter a row"))
# c=int(input("enter a colls"))
# A=[]
# for i in range(r):
#     temp=[]
#     for j in range(c):
#         x=int(input("enter a element"))
#         temp.append(x)
#     A.append(temp)

# r=int(input("enter a row"))
# c=int(input("enter a colls"))
# B=[]
# for i in range(r):
#     temp=[]
#     for j in range(c):
#         x=int(input("enter a element"))
#         temp.append(x)
#     B.append(temp)
# r=len(A)
# c=len(A[0])
# for i in range(r):
#     for j in range(c):
#         # if j==i:
#         #     print(m[i][j],end="")
#         # else:
#         #     print(" ",end="")
#         print(A[i][j]+B[i][j])
       
#     print()
# row=int(input("enter number of rows"))
# cols=int(input("enter number of COLS"))
# A=[]
# for i in range(row):
#     temp=[]
#     for j in range(cols):
#         x=int(input("enter a element"))
#         temp.append(x)
#     A.append(temp)
# row=int(input("enter number of rows"))
# cols=int(input("enter number of cols"))
# B=[]
# for i in range(row):
#     temp=[]
#     for j in range(cols):
#         x=int(input("enter a element"))
#         temp.append(x)
#     B.append(temp)


# r=len(A)
# c=len(A[0])
# for i in range(r):
#     for j in range(c):
#         print(A[i][j]+B[i][j],end=" ")
#     print()

# row1=int(input("enter rows"))
# col1=int(input("enter rows"))
# A=[]
# for i in range(row1):
#     temp=[]
#     for j in range(col1):
#         x=int(input("enter a elemnet"))
#         temp.append(x)
#     A.append(temp)

# row2=int(input("enter a row2"))
# col2=int(input("enter a cols"))
# B=[]
# for j in range(row2):
#     temp=[]
#     for j in range(col2):
#         x=int(input("enter a element"))
#         temp.append(x)
#     B.append(temp)
# total=[]
# for i in range(row1):
#     res=[]
#     for j in range(col2):
#         sum=0
        
#         for k in range(row2):
#             sum=sum+A[i][j]*B[i][k]
#         res.append(sum)
#     total.append(res)
# print(total,end=" ")


#substring
# s=input("entere a string")
# maxi=""
# for i in range(len(s)):
#     sub=""
#     for j in range(i,len(s)):
#         sub=sub+s[j]
#         print(sub)
#         done=""
#         for k in sub:
#             if k not in done:
#                 done = done+k
#         if len(done)==len(sub):
#             if len(sub)>len(maxi):
#                 maxi=sub
# print(maxi)
# s=input("entyer a string")
# long=""
# for i in range(1,len(s)):
#     sub=""
#     for j in range(i):
#         sub=sub+s[j]
#     end=""

#     for k in range(len(s)-len(sub),len(s)):
#         end=end+s[k]
#     if sub==end:
#         if len(sub)>len(long):
#             long=sub
# print(long)


#player
# n=int(input("enter number of players"))
# players=[]
# for i in range(n):
#     playerid=int(input("enter player id"))
#     name=input("enter player name")
#     runs=int(input("enter player runs"))
#     player=(playerid,name,runs)
#     players.append(player)
# print(players)

# highest = players[0]
# lowest = players[0]
# total=0
# for i in players:
#     if i[2] > highest[2]:
#         highest = i
#     if i[2] < lowest[2]:
#         lowest = i
#     total=total+i[2]
# print("Highest:", highest)
# print("Lowest:", lowest)
# print("total:", total)
# avg=total/len(players)
# print("Avarage",avg)

# for i in players:
#     if i[2] > 50:
#         print(i)

#password
# n = int(input("Enter number of passwords"))

# passwords = []

# for i in range(n):
#     s = input("Enter password")
#     passwords.append(s)

# count = 0

# for i in range(len(passwords)):

#     for j in range(i + 1, len(passwords)):

#         a = set(passwords[i])
#         b = set(passwords[j])

#         common = 0

#         for k in a:
#             if k in b:
#                 common = common + 1

#         if common == 0:
#             count = count + 1

# print(count)

#two string
# s1 = input("Enter string 1: ")
# s2 = input("Enter string 2: ")

# count = 0

# if len(s1) == len(s2):

#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             count = count + 1

#     if count == 1:
#         print(True)
#     else:
#         print(False)

# s1 = input("Enter string 1: ")
# s2 = input("Enter string 2: ")

# count = 0

# if len(s1) == len(s2):

#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             count = count + 1

#     if count == 1:
#         print(True)
#     else:
#         print(False)

# elif abs(len(s1) - len(s2)) == 1:

#     if len(s1) > len(s2):
#         big = s1
#         small = s2
#     else:
#         big = s2
#         small = s1

#     i = 0
#     j = 0
#     count = 0

#     while i < len(big) and j < len(small):

#         if big[i] != small[j]:
#             count = count + 1
#             i = i + 1
#         else:
#             i = i + 1
#             j = j + 1

#     if count <= 1:
#         print(True)
#     else:
#         print(False)

# else:
#     print(False)

# s = input("Enter number")

# sum = 0
# largest = 0

# for i in range(len(s) - 1):

#     diff = abs(int(s[i]) - int(s[i + 1]))

#     print(diff, end=" ")

#     sum = sum + diff

#     if diff > largest:
#         largest = diff

# print()
# print("Sum =", sum)
# print("Largest =", largest)

# if sum % len(s) == 0:
#     print("Balanced Number")
# else:
#     print("Unbalanced Number")


d = input("Enter a digit")

done = ""

max_count = 0
max_digit = ""
total = 0

for i in d:

    if i not in done:

        count = 0

        for j in d:
            if i == j:
                count = count + 1

        done = done + i

        if count > 1:
            print(count, i)
            total = total + count

        if count > max_count:
            max_count = count
            max_digit = i

print("Total =", total)
print("Max Frequency =", max_count)
print("Max Digit =", max_digit)