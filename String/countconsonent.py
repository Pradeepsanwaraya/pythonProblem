string=input("enter any string")
count=0
vowel="aeiouAEIOU"
for ch in string:
    if ch not in vowel:
        count=count+1
print(count)
        