# n=[[1,2,3],[4,5,6]]
# r=len(n)
# c=len(n[0])
# result = [[0]*r for i in range(c)]
# for i in range(r):
#     for j in range(c):
#         result[j][i]=n[i][j]
# print(result,end="")
# n=int(input("enter a size"))
# res=[]
# for i in range(n):
#     temp=[]
#     for j in range(n):
#         x=int(input("enter a list"))
#         temp.append(x)
#     res.append(temp)
# print(res)
# r=len(res)
# c=len(res[0])
# for i in range(r):
#     for j in range(c):
#         if j>=i:
#             print(res[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
n=int(input("enter a size"))
res=[]
for i in range(n):
    temp=[]
    for j in range(n):
        x=int(input("enter a list"))
        temp.append(x)
    res.append(temp)
n2=int(input("enter a size"))
res2=[]
for i in range(n2):
    temp2=[]
    for j in range(n2):
        x2=int(input("enter a list"))
        temp2.append(x2)
    res2.append(temp2)
print(res)
r=len(res)
c=len(res[0])
result=[]
for i in range(r):
    temp=[]
    for j in range(c):
        temp.append(res[i][j]+res2[i][j])
    result.append(temp)
print(result)