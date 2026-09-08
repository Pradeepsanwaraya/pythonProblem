# s=input("enter a string")
# for i in range(len(s)):
#     sub=""
#     for j in range(i,len(s)):
#         sub=sub+s[j]
#         print(sub)

# s=input("enter a string")
# for i in range(len(s)):
#     sub=""
#     for j in range(i,len(s)):


#         sub=sub+s[j]
#         if len(sub)==3:
#             print(sub)



# s=input("enter a string")
# count=0
# long=''
# for i in range(len(s)):
#     sub=""
#     for j in range(i,len(s)):


#         sub=sub+s[j]
#         rev=""
#         for r in sub:
#             rev=r+rev
#         if sub==rev:
#             if len(sub)>len(long):
#                 long=sub
# print(long)

# s=input("enter a string")
# count=0
# long=''
# for i in range(len(s)):
#     sub=""
#     for j in range(i,len(s)):


#         sub=sub+s[j]
#         done=""
#         for l in sub:
#             if l not in done:
#                 done=done+l
#         if len(done)==len(sub):
#             if len(done)>len(long):
#                 long=done            
# print(long)

# s=input("enter a string")
# target=input("enter a target")
# count=0
# for i in range(len(s)):
#     sub=""
#     for j in range(i,len(s)):
#         sub=sub+s[j]
#         if len(sub) == len(target):
#             if sub == target:
#                 count += 1
# print(count)


s = input("enter a string")

# long = ""

# for i in range(1, len(s)):

#     sub = ""

#     for j in range(i):

#         sub = sub + s[j]

#     end = ""

#     for l in range(len(s) - len(sub), len(s)):
#         end = end + s[l]

#     if sub == end:

#         if len(sub) > len(long):
#             long = sub

# print(long)
# long=""
# for i in range(1,len(s)):
#     sub=""
#     for j in range(i):
#         sub=sub+s[j]
#     end=""
#     for l in range(len(s)-len(sub),len(s)):
#         end=end+s[l]
#     if sub==end:
#         if len(sub)>len(long):
#             long=sub
# print(long)


# long=""
# for i in range(1,len(s)):
#     sub=""
#     for j in range(i):
#         sub=sub+s[j]
#     end=""
#     for l in range(len(s)-len(sub),len(s)):
#         end=end+s[l]
#     if sub==end:
#         if len(sub)>len(long):
#             long=sub
# print(long)

long=""

for i in range(1, len(s)):

    sub = ""

    for j in range(i):
        sub = sub + s[j]

    end = ""

    for l in range(len(s) - len(sub), len(s)):
        end = end + s[l]

    rev = ""

    for k in end:
        rev = k + rev

    if sub == rev:
        if len(sub) > len(long):
            long = sub

print(long)

print("sub =", sub, "end =", end, "rev =", rev)



















