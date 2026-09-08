# N=int(input("enter elemenrt of dictionary"))
# d={}
# for i in range(N):
#     key=input("enter  a key")
#     value=int(input("enter  a vaalue"))
#     d[key]=value
# print(d)

# for k,v in d.items():
#     print(k,"    ",v)

l=list((input("Enter your n").split()))

d={}
for i in l:
    length=len(i)
    if length not in d:
        d[length]=[]
    d[length].append(i)

print(d)