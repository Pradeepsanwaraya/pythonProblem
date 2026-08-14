from collections import namedtuple

Students=namedtuple("students",["rollno","name","marks"])

n=int(input("enter no of students"))

students=[]

for i in range(n):
    print("students details")

    r=int(input("enter roll no"))
    
    print("students details")
    
    name=input("enter roll no")
    
    print("students details")
    
    m=int(input("enter marks"))
    
    s=Students(r,name,m)
    
    students.append(s)
for x in students:
    
    print(x.rollno,x.name)