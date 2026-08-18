n=[[1,4,7],[2,5,8],[9,6,3]]
r=len(n)
c=len(n[0])
# for i in range(r):
#     for j in range(c):
#         if j>=i:
#             print(n[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
# for i in range(r):
#     for j in range(c):
#         if j<=i:
#             print(n[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
# for i in range(r):
#     for j in range(c):
#         if i==j:
#             print(n[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
# for i in range(r):
#     for j in range(c):
#         if i+j==c-1:
#             print(n[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
# for i in range(r):
#     for j in range(c):
#         if i==j or i+j==c-1:
#             print(n[i][j],end=" ")
#         else:
#             print("*",end=" ")
# #     print()
# for i in range(r):
#     for j in range(c):
#         if i==1 and j==1:
#             print(n[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
for i in range(r):
    for j in range(c):
        if j==0:
            print(n[i][j],end=" ")
        else:
            print("*",end=" ")
    print()