# r=int(input("enter a rows"))
# c=int(input("enter a coulnm"))
# A=[]
# for i in range(r):
#     temp=[]
#     for j in range(c):
#         x=int(input("enter a list"))
#         temp.append(x)
#     A.append(temp)
# B=[]
# for i in range(r):
#     temp=[]
#     for j in range(c):
#         x=int(input("enter a list"))
#         temp.append(x)
#     B.append(temp)
# res=[]
# for i in range(r):
#     temp=[]
#     for j in range(c):
#         temp.append(A[i][j]+B[i][j])
#     res.append(temp)
# print(A)
# print(B)
# print(res)

# r=int(input("enter a rows"))
# c=int(input("enter a cols"))
# a=[]
# for i in range(r):
#     temp=[]
#     for j in range(c):
#         x=int(input("enter a list element"))
#         temp.append(x)
#     a.append(temp)
# b=[]
# for i in range(r):
#     temp=[]
#     for j in range(c):
#         x=int(input("enter list 2"))
#         temp.append(x)
#     b.append(temp)

# res=[]
# for i in range(r):
#     temp=[]
#     for j in range(c):
#         temp.append(a[i][j]-b[i][j])
#     res.append(temp)
# print(res)
r=int(input("enter  areow"))
c=int(input("enter  a column"))
a=[]
for i in range(r):
    temp=[]
    for j in range(c):
        x=int(input("entre a list"))
        temp.append(x)
    a.append((temp))
b=[]
for i in range(r):
    temp=[]
    for j in range(c):
        x=int(input("enter a liost 2"))
        temp.append(x)
    b.append(temp)
res=[]
same=True
for i in range(r):
    temp=[]
    for j in range(c):
        if a[i][j]!=b[i][j]:
            same=False
if same:
    print("both are same")
else: 
    print("both are not same")