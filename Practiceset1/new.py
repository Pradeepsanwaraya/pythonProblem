# s=input("enter a string")
# for i in s:
#     rev=''
#     for j in i:
#         rev=j+rev
#     print(rev,end='')


# s=input("enter a string")
# word=s.split()
# i=0

# while i<len(word):
#     print(word[i][::-1],end=" ")
#     i=i+1

# s=input("enter a string").split()
# for i in s:    
#     print(i[::-1],end=" ")

#a2b3c4
# s=input("enter any string")
# res=''
# pre=''
# for i in s:
#     if i.isalpha():
#         res=res+i
#         pre=i
#     else:
#         res=res+pre*(int(i)-1)
# print(res)
s=input("enter any string")
res='' 
pre=''
for i in s:
    if i.isalpha():
        res=res+i
        pre=i
    else:
        next=chr(ord(pre)+int(i))
        res=res+next

print(res)