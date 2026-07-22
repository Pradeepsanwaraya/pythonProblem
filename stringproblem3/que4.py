
# A messaging application wants to temporarily encrypt messages during
# transmission. The encryption rule is to reverse every word individually
# while keeping the word positions unchanged.

# Input: Enter message: java is powerful

# Output: Encrypted Message: avaj si lufrewop
msg=input("enter any number").split()
rev=msg
for i in range(len(rev)):
    rev[i]=rev[i][::-1]

print(" ".join(rev))
