n=int(input("Entetr the number of student:"))
for i in range(n):
  rollno=int(input("Enter Roll Number:"))
  student_name=input("Enter Student Name:")
  status=input("Enter The Status:") 
  with open("attendence.txt","a") as f:
    f.write(f"{rollno},{student_name},{status}\n")

with open("attendence.txt","r") as f:
  total=0
  present=0
  for line in f:
    total+=1
    parts=line.strip().split(",")
    if parts[2]=="present":
      present+=1
  print("Total Attendence",total) 
  print("Present Student:",present)
  print("Absent student:",total-present)
  print("Attendence percentage: ",(present/total)*100)

