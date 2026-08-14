string=input("enter any para").split()
punctuation=input("enter a punctuation you want to remove")
newstring=""
for i in string:
    for j in punctuation:
        if j!=i:
            newstring=newstring+' '+i

    else:
        newstring=newstring+''
print(newstring)