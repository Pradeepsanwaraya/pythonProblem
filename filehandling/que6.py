
# 6. Find the Longest Word

# A document-processing application needs to identify the longest word in a text document.

# Write a Python program that reads a file named "article.txt" and finds the longest word in the file.

# Input File: article.txt

# Python programming language is powerful.
# Developers use Python for application development.

# Expected Output:

# Longest Word: programming
# Length: 11

lines_count=0
words_count=0
with open ("first.txt","r") as f:
    for line in f:
        # lines_count+=1
        words_count+=len(line.split())
        if lines_count:
print(lines_count)
print(words_count)