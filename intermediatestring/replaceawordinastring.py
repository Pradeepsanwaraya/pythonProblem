string=input("enter a string ").split()
print(string)
replace=input("enter a word that you want to replace ")
print(string)
print(replace)
newworld=input("enter any new world ")

newstring=''
for i in string:
    if i!=replace:
        newstring=newstring+' '+i
    else:
        newstring= newstring+' '+newworld
print(string)
print("replace ", replace)
print(newstring)
