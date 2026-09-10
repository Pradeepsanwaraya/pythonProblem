# s=input("enter a string")
# for i in range(len(s)):
#     sub=""
#     for j in range(i,len(s)):
#         sub=sub+s[j]
#         print(sub)


# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
#         l1=len(word1)
#         l2=len(word2)
#         i=0
#         j=0
#         result=''
#         while i<l1 or j<l2:
#             if i<l1:
#                 result+=word1[i]
#                 i+=1
#             if j<l2:        
#                 result+=word2[j]
#                 j+=1
#         return result

l=input("enter a string 1:")
l2=input("enter a string 2:")
l1=len(l)
l22=len(l2)
i=0
j=0
mg=""
while i<l1 or j<l22:
    if i<l1:
        mg=mg+l[i]
        i=i+1
    if j<l22:
        mg=mg+l2[j]
        j=j+1
print(mg)