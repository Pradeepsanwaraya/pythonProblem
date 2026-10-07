
# 2. Employee Salary Report

# A company stores employee salary information in employees.txt.

# Each record contains:

# EmployeeID,EmployeeName,Department,Salary
# Task

# Write a Python program to:

# Accept employee details.
# Store them in the file.
# Read the file.
# Display employees whose salary is greater than ₹50,000.
# Calculate the average salary.
# Sample Input
# Enter number of employees: 4

# 101,Ajay,IT,65000
# 102,Ravi,HR,45000
# 103,Priya,IT,72000
# 104,Amit,Sales,48000
# Expected Output
# Employees with Salary > 50000
# --------------------------------
# 101  Ajay   IT       65000
# 103  Priya  IT       72000

# Average Salary: 57500.00

# n=int(input("Entetr the number of employee:"))
# for i in range(n):
#   Employeeid=int(input("Enter Empoyee id:"))
#   Employeename=input("Enter Employee Name:")
#   department=input("Enter Employee department:") 
#   salary=int(input("Enter Employee salary:")) 
#   with open("salaryreport.txt","a") as f:
#     f.write(f"{Employeeid},{Employeename},{department},{salary}\n")

# with open("salaryreport.txt","r") as f:
#   for line in f:
#     parts=line.strip().split(",")
#     if int(parts[3])>50000:
#       print((f"{Employeeid},{Employeename},{department},{salary}\n"))
#       break

n=int(input("enter number of employees:"))
for i in range(n):
    employeeid=int(input("enter employee id:"))
    employeename=input("enter employee name:")
    department=input("enter employee department:")
    salary=int(input("enter employee salary:"))
    with open("employees.txt","a") as f:
        f.write(f"{employeeid},{employeename},{department},{salary}\n")
total=0
count=0
print("employees with salary > 50000")
print("--------------------------------")
with open("employees.txt","r") as f:
    for line in f:
        parts=line.strip().split(",")
        salary=int(parts[3])
        total+=salary
        count+=1
        if salary>50000:
            print(f"{parts[0]}  {parts[1]}  {parts[2]}  {parts[3]}")

average=total/count

print("average salary:",average)