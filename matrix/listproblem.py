# l=[1,2,45,7,8,9]
# mini=l[0]
# maxi=l[0]
# for i in l:
#     if i>maxi:
#         maxi=i
#     if i<mini:
#         mini=i
# print(maxi,mini)
# secondhighest
# l=[1,4,5,2,6,3,7]
# maxi=l[0]
# for i in l:
#     if i>maxi:
#         maxi=i
# l.remove(maxi)
# second=l[0]
# for i in l:
#     if i>second:
#         second=i
# print(second)
# l=[1,4,5,2,6,3,7]
# maxi=l[0]
# second=l[0]
# for i in l:
#     if i>maxi:
#         second=maxi
#         maxi=i
#     elif i>second and i!=maxi:
#         second=i
# l = [1, 4, 5, 2, 6, 3, 7]

# mini = l[0]
# sec = l[1]

# for i in l[2:]:
#     if i < mini:
#         sec = mini
#         mini = i
#     elif i > mini and i < sec:
#         sec = i

# print(sec)
# l=[1,14,25,15,5,4,7,52,1,2,1,3,5,6]

# done=[]
# for i in l:
#     if i not in done:
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         done.append(i)
#         print(count,i)
# l=[1,14,25,15,5,4,7,52,1,2,1,3,5,6]
# done=[]
# for i in l:
#     if i not in done:
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         done.append(i)
#         if count>1:
#             print(count,i)
#             break
# l=[1,14,25,15,5,4,7,52,1,2,1,3,5,6]
# done=[]
# for i in l:
#     if i not in done:
#         count=0
#         for j in l:
#             if i==j:
#                 count=count+1
#         done.append(i)
#         if count==1:
#             print(count,i)
#             break
# l=[1,5,7,8,5,2,6,3]
# target=9
# count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             count=count+1
#             print(l[i],l[j])
# print(count)

# l = [1, 5, 3, 4, 2, 6, 8]
# count = 0
# target=2
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if abs(l[i]-l[j])==target:
#             count=count+1
#             print(l[i],l[j])
# print(count)
l = [-2, 1, -3, 4, -1, 2, 1]
som=0
for i in range(len(l)):
    current_sum = 0

    for j in range(i, len(l)):
        current_sum = current_sum + l[j]
        if current_sum>som:
            som=current_sum
print(som)