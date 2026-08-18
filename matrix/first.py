n=[[1,2,3],[3,6,9],[7,4,1]]
r=len(n)
col=len(n[0])
# for i in range(r):
#     for j in range(col):
#         print(n[i][j],end=" ")
#     print()

# for i in range(r):
#     for j in range(col):
#         if j>=i:
#             print(n[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
# for i in range(r):
#     for j in range(col):
#         if j<=i:
#             print(n[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()
for i in range(r):
    for j in range(col):
        if i==j:
            print(n[i][j],end=" ")
        else:
            print("*",end=" ")
    print()