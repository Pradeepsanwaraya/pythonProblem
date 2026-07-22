stri="python uis programming lsngusge"
vowels="aeiou"
count=0
for char in stri:
    if char.lower() in vowels:
        count=count+1
print(count)