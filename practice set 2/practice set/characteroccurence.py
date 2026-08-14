# character=input("enter any character")
# done=""
# count=0
# for i in character:
#     if i not in done:
#         count=0
#         for j in character:
#             if i==j:
#                 count=count+1
#         print(i,count)
#         done=done+i

string=input("enter any string")
character=input("enter any character")
count=0
for i in string:
    if i==character:
        count=count+1
print(count)