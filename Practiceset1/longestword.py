sentence="pradeep is the small and long"
words=sentence.split()
longest=""
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)