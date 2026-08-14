# Question 5 – Advanced Password Security Checker

# Ye pehla real interview type question hai.

# Password valid tab hoga jab:
# Start uppercase letter se ho.
# End digit se ho.
# Kam se kam 2 digits ho.
# Kam se kam 1 special character ho (@ # $ % & *)
# Space na ho.
# Length 8 se 15 ke beech ho.
pas=input("enter any string")
count=0
digit=0
l=0
c=0
s=0
sc=0
for i in pas:
    if len(pas)>=8 and len(pas)<=15:
        
        digit=digit+1

    elif pas[0]>='A' and pas[0]<='Z':
        ch=ch+1
    elif pas[-1]>='0' and pas[-1]<='9':
        d=d+1
        
    elif i==' ':
        s=s+1
        
    elif i=='@' or i=='#' or i=='$' or i=='%' or i=='*':
        sc=sc+1
    else:
        pass
    
if count==5 and digit==2:
    print("valid password")
else:
    print("invalid password")