string=input("enter any string")
count=0
vowel="aeiouAEIOU"
for i in string:
    if i in vowel:
        count=count+1
print(count)