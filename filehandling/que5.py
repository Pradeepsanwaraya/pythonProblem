# 5. Count Vowels and Consonants
# A language-learning application wants to analyze the characters used in a paragraph.

# Write a Python program that reads a file named "paragraph.txt" and counts:

# 1. Total number of vowels
# 2. Total number of consonants

# Ignore numbers, spaces and special characters.

# Input File: paragraph.txt

# Python Programming is Interesting.

# Expected Output:

# Total Vowels: <display count>
# Total Consonants: <display count>

def vowelcount():
    file=open("first.txt","r")
    content=file.read()
    count=0
    consonent=0
    vowels=list("AEIOUaeiou")
    for vowel in content:
        if vowel in vowels:
            count+=1
        else:
            consonent+=1
    return count,consonent
print(vowelcount())


lines_count=0
words_count=0
with open ("first.txt","r") as f:
    for line in f:
        lines_count+=1
        words_count+=len(line.split())
print(lines_count)
print(words_count)

# file=open("abc.txt","r+")
# content=file.read()
# file.write("my name is prince panwar")
# print(content)
# file=open("abc.txt","r")
# content=file.read()
# print(content)

# file = open("abc.txt","w+")
# content=file.write("the earth this is shreya  and ")
# # file.seek(3)
# content=file.read()
# print(content)

# file = open("pq.txt","a+")
# content=file.write(" hey prince panwar")
# file.seek(0)
# content=file.read()
# # print(content)
# import os

# f1=open("images.jpg","rb")
# data=f1.read()
# f1.close()

# print(data)

# f2=open("images.jpg","ab")
# f2.write(data)
# f2.close()

# os.startfile("images.jpg")


lines_count=0
words_count=0
with open ("first.txt","r") as f:
    for line in f:
        lines_count+=1
        words_count+=len(line.split())
print(lines_count)
print(words_count)