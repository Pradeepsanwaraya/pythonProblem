# s = input("Enter string: ").split()
# target = input("Enter word: ")

# for i in range(len(s)-1,-1,-1):
#     if s[i] == target:
#         s[i] = ""

# for i in s:
#     if i != "":
#         print(i, end=" ")


# s = input("Enter string: ").split()
# target = input("Enter word: ")
# newword = input("Enter word: ")

# for i in range(len(s)-1,-1,-1):
#     if s[i] == target:
#         s[i] = newword

# for i in s:
#     if i != "":
#         print(i, end=" ")


# s = input("Enter string: ").split()
# done=""
# new=""
# for i in s:
#     if i not in done:
#         for j in s:
#             if i == j:
#                 pass
#         done=done+i+" "
# print(done)



# s = input("Enter string: ").split()
# done=""
# new=""
# for i in s:
#     if i not in done:
#         count=0
#         for j in s:
#             if i == j:
#                 count=count+1
#         done=done+i+" "
#         if count>0:
#             print(count,i)


# s = input("Enter string: ").split()
# done=""
# new=9
# for i in s:
#     if len(i)<new:
#         new=len(i)
#         done=i
# print(done,new)


# s = input("Enter string: ").split()

# for i in s:
#     if i == i[::-1]:
#         print(i)
#         break


# s=input("enter a string").split()
# done=""
# for i in s:
#     done=i+" "+done
# print(done)

# s=input("enter a string").split()
# rev=""
# for i in s:
#     done=""
#     for j in i:
#         done=j+done
#     rev=rev+done+" "
# # print(rev)


# s=input("enter a string")
# rev=""
# word=""
# for i in s:
#     if i==" ":
#         rev=word+" "+rev
#         word=""
#     else:
#         word=word+i
# rev=word+" "+rev
# print(rev)