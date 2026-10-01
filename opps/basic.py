# class Student:
#     def __init__(self):
#         print("hello")
#     def show(self,name,address):
#         print(name,address)
#     def display(self,cl,df):
#         print(cl,df)
#         print(self.name,self.address)

# obj=Student()
# obj.show("pradeep","dhar")
# obj.display("op","em")

# class Child:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def show(self):
#         print(self.name)
#         print(self.address)
# class Parent(Child):
#     def __init__(self,name,address,contact,aadhar):
#         super().__init__(name,address)
#         self.contact=contact
#         self.aadhar=aadhar
#     def display(self):
#         print(self.contact)
#         print(self.aadhar)
#         print(self.name)

# obj=Parent("pradep","dhar",7845,96578)
# obj.show()
# obj.display()

# class Parent:
#     def show(self):
#         print("method of parent class")
# class Child(Parent):
#     def __init__(self):
#         print("constroctor of child")
#     def display(self):
#         super().show()
#         print("method of child")
# obj=Child()
# obj.display()


# class A:
#     def show(self):
#         print("a")
# class B(A):
#     def show(self):
#         super().show()
#         print("b")
# class C(B):
#     def show(self):
#         super().show()
#         print("c")
# obj=C()
# obj.show()
  
# class Student:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def show(self):
#         print(self.name)
#         print(self.address)
# class College(Student):
#     def __init__(self,name,address,course):
#         super().__init__(name,address)
#         self.course=course
#     def display(self):
#         print(self.course)
#         print(self.name)
#         print(self.address)
# obj=College("pradeep","dhar","mca")
# obj.show()
# obj.display()