# 1.  Bank Customer Account Privacy System
# A national bank is developing a secure customer portal where account
# numbers should not be displayed completely on the screen. For security
# reasons, the system should hide all digits except the last four digits
# before showing them to users.
# Conditions: - Display only the last 4 digits - Replace all previous
# characters with *
# Input: Enter account number: 123456789012
# Output: Masked Account: ********9012
number=input("enter account number")
star=''
count=0
lastd=''
for i in number:
    count=count+1
for i in range(count):
    if i<count-4:
        star=star+'*'
    else:
        lastd=lastd+number[i]
print(star+lastd)