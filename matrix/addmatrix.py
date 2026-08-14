row=int(input("enter a row"))
col=int(input("enter a column"))
A=[]
for i in range(row):
    temp=[]
    for j in range(col):
        x=int(input("enter a list"))
        temp.append(x)
    A.append(temp)

row=int(input("enter a row"))
col=int(input("enter a column"))
B=[]
for i in range(row):
    temp=[]
    for j in range(col):
        x=int(input("enter a list"))
        temp.append(x)
    B.append(temp)
print(B)
res=[]
for i in range(row):
    trep=[]
    for j in range(col):
        trep.append(A[i][j]+B[i][j])
    res.append(trep)
print(res)
