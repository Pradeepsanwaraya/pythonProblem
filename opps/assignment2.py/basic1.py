# class Student:
#     def details(self):
#         self.name="pradeep"
#         self.age=23
#         self.corse="Bca"
#         print(self.name,self.age,self.corse)
# obj=Student()
# obj.details()
# # "self is a reference to the current object of the class.
# #  It is used to access the instance variables and methods of that object."
# class Student:

#     def show(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#         print(self.name,self.age,self.course)
# obj=Student()
# obj2=Student()
# obj.show("pradeep",23,"Bca")
# obj2.show("Ravi",24,"Bca")

# class Student:

#     dep="IIST "
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     def show(self):
#         print(self.dep,self.name,self.age,self.course)
# obj=Student("pradeep",23,"Bca")
# obj2=Student("Ravi",22,"Bca")
# obj.show()
# obj2.show()

# class Employee:
#     def __init__(self,name,salary,department):
#         self.name=name
#         self.salary=salary
#         self.department=department
#     def salaryinc(self):
#         self.salary=self.salary+5000
#     def show(self):
#         print(self.name)
#         print(self.salary)
#         print(self.department)
#         # print(self.increase)
# obj=Employee("Pradeep",10000,"data")
# obj2=Employee("Ravi",20000,"data")
# obj.salaryinc()
# obj2.salaryinc()
# obj.show()
# obj2.show()

# class Employee:
#     company="tcs"
#     def __init__(self,name):
#         self.name=name
#         # self.company=company
#     def show(self):
#         print(self.name,self.company)

# obj=Employee("pradeep")
# obj2=Employee("Ravi")
# obj.show()
# Employee.company="infobeans"
# obj.show()
# obj2.show()

# class Employee:
#     company = "Infobeans"
#     total_employees = 0

#     def __init__(self, emp_id, name, department, salary):
#         self.emp_id=int(input("enter your name"))
#         self.name=input("enter your name")
#         self.department=input("enter your department")
#         self.salary=int(input("enter your salary"))

#     def show_details(self):
        
#         print(f"{self.emp_id},{self.name},{self.department},{self.salary}")

#     def give_raise(self, percent):
#         self.salary=self.salary+(self.salary*percent/100)

#     def annual_salary(self):
#         self.salary=self.salary*12


# # Test code
# e1 = Employee(101, "Pradeep", "Development", 30000)
# e2 = Employee(102, "Rahul", "Testing", 25000)
# e3 = Employee(103, "Amit", "Development", 35000)

# e1.show_details()
# e2.show_details()

# e1.give_raise(10)
# print("Raise ke baad:", e1.salary)
# print("Saalana salary:", e1.annual_salary())

# print("Total employees:", Employee.total_employees)

# class Student:
#     school="infobeans"
#     total_student=0
#     def __init__(self,rollno,name,marks):
#         self.rollno=rollno
#         self.name=name
#         self.marks=marks
#         Student.total_student+=1
#     def is_pass(self):
#         return self.marks > 40
#     def details(self):
        
#         print(f"!student name is {self.name} !rollno is {self.rollno} !tital marks is {self.marks} ")
#         print("number of student",self.total_student)
#         print("marks is greater than 40",self.is_pass())
# obj=Student(101,"pradeep",450)
# obj1=Student(102,"pradeep sanwaraya",490)
# obj.details()
# obj1.details()
# obj2 = Student(103, "Rahul", 495)
# l = [obj, obj1, obj2]
# topper=l[0]
# for i in l:
#     print(i.name,i.marks)
#     if i.marks>topper.marks:
#         topper=i
# print("topper is :",topper.name,topper.marks)

class BankAccount:
    bank="infobeans"
    total_