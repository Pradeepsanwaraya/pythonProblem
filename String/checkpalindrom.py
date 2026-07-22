string=input("enter any string")
revstring=string
rev=''
for i in range(len(string)-1,-1,-1):
    rev=rev+string[i]
if revstring==rev:
    print("palindrom")
else:
    print("not a palindrom")