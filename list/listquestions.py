# Phase 1: Python List Mastery (Foundation)
# Traversal
#  Print all elements
#  Print using index
#  Reverse traversal



#  Sum of elements
#  Product of elements
#  Average
#  Count even
#  Count odd
#  Count positive
#  Count negative
#  Count zero
# Searching
#  Linear Search
#  Search with index
#  Search all indexes
#  Count occurrences
#  First occurrence
#  Last occurrence
# Maximum / Minimum
#  Largest element
#  Smallest element
#  Largest with index
#  Smallest with index
#  Second largest
#  Second smallest
# Array Modification
#  Multiply all by 2
#  Square every element
#  Replace negative with 0
#  Replace even with 0
#  Add 10 to every element
#  Reverse list (without reverse())two pointer
# 🟡 Phase 2: List Methods
#  append()
#  extend()
#  insert()
#  pop()
#  remove()
#  clear()
#  index()
#  count()
#  reverse()
#  sort()
#  copy()
# 🟠 Phase 3: Strings for DSA
#  Traverse string
#  Count vowels
#  Count consonants
#  Count digits
#  Count spaces
#  Reverse string
#  Palindrome
#  Frequency of character
#  First non-repeating character
# 🔵 Phase 4: Matrix (2D List)
#  Traverse matrix
#  Row sum
#  Column sum
#  Diagonal sum
#  Largest element
#  Transpose
# 🟣 Phase 5: Pattern Recognition
#  Frequency array
#  Prefix Sum
#  Two Pointer
#  Sliding Window (Basics)
# 🔴 Phase 6: LeetCode Easy Arrays
#  Two Sum
#  Contains Duplicate
#  Remove Duplicates from Sorted Array
#  Merge Sorted Array
#  Move Zeroes
#  Best Time to Buy and Sell Stock
#  Maximum Subarray (Kadane)
#  Plus One
#  Find Pivot Index
#  Running Sum
#  Richest Customer Wealth
# 🟤 Phase 7: HashMap / Dictionary
#  Frequency Counter
#  Duplicate Detection
#  Character Count
#  Two Sum (HashMap)
#  Anagram
# ⚫ Phase 8: Stack
#  Stack using list
#  Valid Parentheses
#  Min Stack
# ⚪ Phase 9: Queue
#  Queue Basics
#  Circular Queue Basics
# 🟢 Phase 10: Linked List
#  Traverse
#  Insert
#  Delete
#  Reverse Linked List
#  Middle Node
# 🔵 Phase 11: Recursion
#  Print 1 to N
#  Print N to 1
#  Factorial
#  Fibonacci
#  Sum of N
#  Reverse String
# 🟣 Phase 12: Sorting
#  Bubble Sort
#  Selection Sort
#  Insertion Sort
#  Merge Sort
#  Quick Sort (Basics)
# 🔴 Phase 13: Binary Search
#  Binary Search
#  First Occurrence
#  Last Occurrence
#  Search Insert Position
#  Square Root
# ⚫ Phase 14: Trees
#  DFS
#  BFS
#  Inorder
#  Preorder
#  Postorder
# 🟤 Phase 15: Graph (Basics)
#  BFS
#  DFS
#  Number of Islands
# 🎯 Total
# 100+ practice questions
# 50+ LeetCode Easy
# 30+ LeetCode Medium
# Complete DSA foundation for interviews
# 📌 Mera Plan

# name=[10,20,30,40,50]
# start=0
# end=len(name)-1
# while start<end:
#     temp=name[start]
#     name[start]=name[end]
#     name[end]=temp
#     start=start+1
#     end=end-1

# num=[10,20,30,40,50]
# target=int(input("Enter Target Value : "))
# count=0
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if num[i]+num[j]==target:
           
#             count=count+1
#             print(count)

# if count==0:
#     print("No Pair Found ")
# else:
#     print("Pair Found ",count)

# print(name)




# Main tumhe sirf syntax nahi, balki har topic is order me padhane wala hoon:

# Concept
# Dry Run
# 5–10 Practice Questions
# DSA Pattern
# LeetCode Question
# Homework

# Is tarah padhoge to tum Python bhi strong ka
# roge aur DSA bhi, aur baad me LeetCode solve karna kaafi natural lagega.

# reverse
# l=[10,20,30,40]
# res=[]
# for i in range(len(l)-1,-1,-1):
#     res.append(l[i])
# print(res)

#reverse
# l1=list(map(int,input("Enter Your List ").split())) 

# print("Your  List ")
# print(l1)

# start=0
# end=len(l1)-1
# while start<end:
#     temp=l1[start]
#     l1[start]=l1[end]
#     l1[end]=temp
#     start=start+1
#     end=end-1

# print("Reverse List ")
# print(l1)

# marks=[100,35,36,48,58]

# target=5

# for i in range(len(marks)):
#     if marks[i]==target:
#         print("Element found  at index ",i)
#         break
# else:
#     print("Not Found ")

# marks=[100,20,30,70,50,60]
# min=marks[0]
# print("Before Sorting ")
# print(marks)
# for i in range(len(marks)):
#     for j in range(i+1,len(marks)):
#          if marks[i]>marks[j]:
#               temp=marks[i]
#               marks[i]=marks[j]
#               marks[j]=temp
# print("After Sorting ")
# print(marks)




# a=[10,20,110,10,30]
# b=[10,30,20,50]
# c=[]
# for i in a:
#     if i not in c:
#         if i in b:
#             c.append(i)
# print(c)

# a=[10,20,4,10,20]
# b=[20,10,50,6,70]
# c=a+b
# res=[]
# for i in c:
#     if i not in res:
#         res.append(i)
# print(res)
# a=[10,20,30,40,50,60]
# res=0
# for i in range(0,len(a),2):

#     res=res+a[i]
# print(res)
# a=[10,20,30,40,90]
# res=[]
# for i in a:
#     res=[i]+res

# print(res)
# l=[10,20,30,50,71,90,45,96,78,42]
# max=l[0]
# for i in l:
#     if max<i:
#         max=i


# print(max)
# l=[0,20,40,0,45,0,60,0]
# z=[]
# n=[]
# for i in l:
#     if i==0:
#         z.append(i)
#     else:
#         n.append(i)
# res=n+z
# print(res)

# a=[10,50,60,7,2,89]
# res=a[0]
# for i in a:
#     if res>i:
#         res=i
# print(res)

# l=[10,4,50,40,10,30,20,30]
# u=[]
# for i in l:
#     if i not in u:
#         u.append(i)

# print(u)
# arr=list(map(int,input("enter a list").split()))
# n=len(arr)
# if n==0:
#     print(-1)
# else:
#     leadersum=0
#     count=0
#     sq=0
#     new=[]
#     factsum=0
    
#     for i in range(n):
#         leader=True
        
#         for j in range(i+1,n):
#             if arr[i]<=arr[j]:
#                 leader=False
#                 break
#         if leader:
#             fact=1
#             for k in range(1,arr[i]+1):
#                 fact=fact*k
#             print(fact)
#             factsum=factsum+fact
#             new.append(arr[i])
#             leadersum=leadersum+arr[i]
#             count=count+1
#             sq=sq+arr[i]*arr[i]
# print(leadersum)
# print(count)
# print(sq)
# print(new)
# print(factsum)
# 1.
# Mountain Hiking Elevation Analysis

# Problem Statement

# A trekking company records the elevation (in meters) reached by a hiker at different checkpoints during a mountain climb.

# A checkpoint is considered a peak checkpoint if its elevation is not smaller than its adjacent checkpoints.

# Given an array elevation[] of size N, find the index of any one peak checkpoint.

# Test Case 1
# arr=list(map(int,input("enter a list").split()))
# n=len(arr)
# peak=-1
# for i in range(n):
#     if i==0:
#         if n==1 or arr[i]>=arr[i+1]:
#             peak=i
#             break
#     elif i==n-1:
#         if arr[i]>=arr[i-1]:
#             peak=i
#             break
#     else:
#         if arr[i]>=arr[i+1] and arr[i]>=arr[i-1]:
#             peak=i
#             break
# if peak!=-1:
#     print(arr[peak])
# else:
#     print("no peak found")


# arr=list(map(int,input("enter a list").split()))
# n=len(arr)
# peak=[]
# for i in range(n):
#     if i==0:
#         if n==1 or arr[i]>=arr[i+1]:
#             peak.append(arr[i])
#         elif i==n-1:
#             if arr[i]>=arr[i-1]:
#                 peak.append[arr[i]]
#         else:
#             if arr[i]>=arr[i+1] and arr[i]>=arr[i-1]:
#                 peak.append(arr[i])
# print(peak)

# Input:
# elevation = [1200, 1450, 1700, 1600, 1500]

# Output:
# 2

# Explanation:
# 1700 is greater than both adjacent values 1450 and 1600.

# Test Case 2

# Input:
# elevation = [800, 900, 950, 1000]

# Output:
# 3

# Explanation:
# Last element can also be a peak because it has no right neighbor.

# Test Case 3

# Input:
# elevation = [3000]

# Output:
# 0

# Explanation:
# Single element is always a peak.


# 2.
# Smart City Traffic Peak Load Analyzer

# Problem Statement

# A smart city monitors traffic density at different time intervals in a day.

# An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

# You are given an array traffic[] of size N.

# Tasks:

# Find all peak elements
# Calculate the sum of all peak traffic values
# Find the product of all peak traffic values
# Return the maximum peak value

# arr=list(map(int,input("enter a list").split()))
# peak=[]
# n=len(arr)
# sum=0
# product=1
# maxi=-1
# for i in range(n):
#     if i==0:
#         if n==1 or arr[i]>=arr[i+1]:  
#             peak.append(arr[i])
#             sum=sum+arr[i]
#             product=product*arr[i]
#             if arr[i]>=maxi:
#                 maxi=arr[i]
#     elif i==n-1:
#         if arr[i]>=arr[i-1]:
#             peak.append(arr[i])
#             sum=sum+arr[i]
#             product=product*arr[i]
#             if arr[i]>=maxi:
#                 maxi=arr[i]
#     else:
#         if arr[i]>=arr[i+1] and arr[i]>=arr[i-1]:
#             peak.append(arr[i])
#             sum=sum+arr[i]
#             product=product*arr[i]
#             if arr[i]>=maxi:
#                 maxi=arr[i]

# print(peak)
# print(sum)
# print(product)
# print(maxi)


# Note:
# If only one element exists, it is the only peak.

# Test Case 1

# Input:
# traffic = [10, 50, 30, 70, 60, 90, 80]

# Output:
# Peaks = [50, 70, 90]
# Sum = 210
# Product = 315000
# Max Peak = 90

# Test Case 2

# Input:
# traffic = [100, 200, 150, 180, 170]

# Output:
# Peaks = [200, 180]
# Sum = 380
# Product = 36000
# Max Peak = 200

# Test Case 3

# Input:
# traffic = [5]

# Output:
# Peaks = [5]
# Sum = 5
# Product = 5
# Max Peak = 5

# 3.
# Industrial Sensor Peak Energy Monitoring System

# Problem Statement

# A factory machine records energy consumption at regular intervals.

# A peak is defined as a value greater than or equal to its neighbors.

# Tasks:

# Find all peak energy values
# Compute sum of squares of peak values
# Compute average of peak values
# Return difference between max peak and min peak
# # If no peaks, return -1
# import sys
# arr=list(map(int,input("enter a string").split()))
# peak=[]
# n=len(arr)
# sum=0
# max=arr[0]
# mini=sys.maxsize
# peakf=False
# for i in range(n):
    
#     if i==0:
#         if n==1 or arr[i]>=arr[i+1]:
#             peakf=True
#             peak.append(arr[i]) 
#             sum=sum+(arr[i]*arr[i])
            
#             mini=arr[i] 
            
#             max=arr[i]
            
#     elif i==n-1:
         
#          if arr[i]>=arr[i-1]:
#             peak.append(arr[i]) 
#             peakf=True
#             sum=sum+(arr[i]*arr[i])
#             if arr[i]<=mini:
#                 mini=arr[i] 
#             if arr[i]>=max:
#                 max=arr[i]
#     else:
#         if arr[i]>=arr[i+1] and arr[i]>=arr[i-1]:
#             peakf=True
#             peak.append(arr[i]) 
#             sum=sum+(arr[i]*arr[i])
#             if arr[i]<=mini:
#                 mini=arr[i] 
#             if arr[i]>=max:
#                 max=arr[i]
# if peakf:
#     diff=int(max-mini)
#     print(max)
#     print(mini)
#     print(peak)
#     print(sum)
#     print(diff)
# arr=list(map(int,input("enter a string").split()))
# peak=[]
# n=len(arr)
# for i in range(n):
#     if i==0:
#         if n==1 or arr[i]>=arr[i+1]:
#             peak.append(arr[i])
#     elif i==n-1:
#         if arr[i]>=arr[i]:
#             peak.append(arr[i])
#     else:
#         if arr[i]>=arr[i+1] and arr[i]>=arr[i-1]:
#             peak.append(arr[i])
# mini=peak[0]
# max=peak[0]
# sum=0
# for i in peak:
#     sum=sum+(i*i)
#     if i<=mini:
#         mini=i
#     if i>=max:
#         max=i
# print(peak)
# print(sum)
# print(mini)                                                                                                                                                                                                       
# print(max)
# print(max-mini)
 
 
# Test Case 1

# Input:
# energy = [20, 40, 30, 60, 50]

# Output:
# Peaks = [40, 60]
# Sum of squares = 5200
# Average = 50
# Difference = 20

# Test Case 2

# Input:
# energy = [10, 20, 15, 25, 20, 30]

# Output:
# Peaks = [20, 25, 30]
# Sum of squares = 1525
# Average = 25
# Difference = 10

# Test Case 3

# Input:
# energy = [5]

# Output:
# Peaks = [5]
# Sum of squares = 25
# Average = 5
# Difference = 0

# 4.

# Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)

# Definition

# A company collects daily performance scores of employees. However, the dataset may contain invalid entries.

# An element is called a leader if:

# It is greater than all elements to its right side
# The element must be valid, i.e., it should not be:
# Negative number
# Zero

# Rightmost valid element is always considered a leader.

# Input Format
# First line → integer n
# Second line → n space-separated integers

# Output Format
# Single integer → sum of all valid leader elements
# If no valid elements exist → return -1

# Rules
# Before finding leaders:

# Ignore all negative values and zeros
# Work only on positive numbers
# Then find leaders from the filtered sequence

# Test Case 1

# Input:
# 8
# 16 0 17 4 -3 3 5 2

# Processing:
# Filtered array:
# [16, 17, 4, 3, 5, 2]

# Leaders:
# [17, 5, 2]

# Output:
# 24

# Test Case 2

# Input:
# 6
# -1 0 -5 0 -2 -3

# Output:
# -1

# Test Case 3

# Input:
# 5
# 10 20 30 40 50

# Processing:
# Filtered array:
# [10, 20, 30, 40, 50]

# Leaders:
# [50]

# Output:
# 50


# 5.
# Given an unsorted array arr[] of size N having both negative and positive integers.
# The task is place all negative element at the end of array without changing the order of positive element and negative element.

# Example 1:
# Input :
# N = 8
# arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
# Output :
# 1  3  2  11  6  -1  -7  -5

# Example 2:
# Input :
# N=8
# arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
# Output :
# 7  9  10  11  -5  -3  -4  -1


# 6.

# A security system logs employee entry IDs during a day.

# Only prime-numbered IDs are considered valid VIP entries.

# Tasks:

# Extract all prime IDs from the list
# Find the sum of prime IDs
# Find the maximum prime ID
# Count how many prime entries exist

# Input:
# A list of integers (may contain duplicates and non-prime numbers)

# Example 1

# Input:
# [12, 5, 7, 9, 11, 14, 17]

# Output:
# Prime IDs = [5, 7, 11, 17]
# Sum = 40
# Max = 17
# Count = 4

# Example 2

# Input:
# [4, 6, 8, 10]

# Output:
# Prime IDs = []
# Sum = 0
# Max = -1
# Count = 0

# 7.
# Factory Production – Factorial Expansion List

# Problem Statement

# A factory produces items where production capacity is defined using factorial growth.

# Given a list of numbers, replace each number with its factorial value.

# Then perform analysis on the resulting list.

# Tasks:

# Convert each element to factorial
# Find sum of all factorial values
# Find maximum factorial value
# Count how many factorial values are even

# Input:
# A list of integers

# Example 1

# Input:
# [3, 4, 5]

# Processing:
# 3! = 6
# 4! = 24
# 5! = 120

# Output:
# [6, 24, 120]
# Sum = 150
# Max = 120
# Even Count = 3
# arr=list(map(int,input("enter a list").split()))
# n=len(arr)
# i=n-1
# last=arr[n-1]
# while i>0:
#     arr[i]=arr[i-1]
#     i=i-1
# arr[0]=last
# print(arr)

# arr=list(map(int,input("enter a list").split()))
# target=int(input("enter your target"))
# n=len(arr)
# count=0
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]+arr[j]==target:
#             count=count+1
# print(count)
# arr=list(map(int,input("enter aa striing").split()))
# target=int(input("enter a string"))
# count=0
# for i in arr:
#     for j in i:
#         if i+j==target:
#             count=count+1
# print(count)  