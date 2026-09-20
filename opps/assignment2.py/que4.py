

# Question 4: Student Result Processing System
# Scenario

# A college wants to automate result generation by calculating total marks, percentage, and grade.

# Requirements

# Create a class named Student with:

# roll_number
# student_name
# marks1
# marks2
# marks3

# Initialize the values using a constructor.

# Calculations
# Total = Marks1 + Marks2 + Marks3
# Percentage = Total / 3
# Grade Criteria
# Percentage Grade
# 90 and above A
# 75 to 89 B
# 60 to 74 C
# Below 60 D
# Sample Input
# Enter Roll Number : 101
# Enter Student Name : Priya Sharma
# Enter Marks in Subject 1 : 85
# Enter Marks in Subject 2 : 90
# Enter Marks in Subject 3 : 88
# Sample Output
# ------ Student Result ------
# Roll Number      : 101
# Student Name     : Priya Sharma
# Total Marks      : 263
# Percentage       : 87.67
# Grade            : B
class Students:
    def __init__(self):
        
        self.roll_number=int(input("enter your rolll no"))
        self.student_name=input("enter your name")
        self.marks1=int(input("enter a subject 1 marks :"))
        self.marks2=int(input("enter a subject 2 marks :"))
        self.marks3=int(input("enter a subject 3 marks :"))
    def calculations(self):
        self.total=self.marks1+self.marks2+self.marks3
        self.percentage=self.total/3
    def grade(self):
        if self.percentage>=90:
            self.grades= "A"
        elif self.percentage>=85:
            self.grades="B"
        elif self.percentage>=60:
            self.grades="C"
        else:
            self.grades="D"
    def display(self):
        print("Roll Number",self.roll_number)
        print("Student Name",self.student_name)
        print("Total Marks",self.total)
        print("Percentage",self.percentage)
        print("Grade",self.grades)
obj1=Students()
obj1.calculations()
obj1.grade()
obj1.display()