# ===== Student Data =====
name = "Pradeep"
course = "BCA"
semester = 6
attendance = 87
python = 85
java = 78
dbms = 90
total_fee = 35000
paid_fee = 25000
books = 2
fine = 100

while True:
    print("\n======================================")
    print("         COLLEGE ERP SYSTEM")
    print("======================================")

    enroll = input("Enter Enrollment Number: ")
    password = input("Enter Password: ")

    if enroll == "1234" and password == "2345":

        while True:
            print("\n========== MENU ==========")
            print("1. Student Profile")
            print("2. Attendance")
            print("3. Marks")
            print("4. Fee")
            print("5. Library")
            print("6. Update Profile")
            print("7. Logout")

            choice = int(input("Enter your choice: "))

            match choice:

                case 1:
                    print("\n===== STUDENT PROFILE =====")
                    print("Name      :", name)
                    print("Course    :", course)
                    print("Semester  :", semester)

                case 2:
                    print("\n===== ATTENDANCE =====")
                    print("Attendance :", attendance, "%")

                    if attendance >= 75:
                        print("Eligible for Exam")
                    else:
                        print("Not Eligible for Exam")

                case 3:
                    print("\n===== MARKS =====")
                    total = python + java + dbms
                    percentage = total / 3

                    print("Python :", python)
                    print("Java   :", java)
                    print("DBMS   :", dbms)
                    print("Total  :", total)
                    print("Percentage :", round(percentage, 2))

                    if percentage >= 90:
                        print("Grade : A+")
                    elif percentage >= 75:
                        print("Grade : A")
                    elif percentage >= 60:
                        print("Grade : B")
                    elif percentage >= 40:
                        print("Grade : C")
                    else:
                        print("Result : Fail")

                case 4:
                    due = total_fee - paid_fee

                    print("\n===== FEE DETAILS =====")
                    print("Total Fee :", total_fee)
                    print("Paid Fee  :", paid_fee)
                    print("Due Fee   :", due)

                case 5:
                    print("\n===== LIBRARY =====")
                    print("Books Issued :", books)
                    print("Fine         :", fine)

                case 6:
                    while True:
                        print("\n===== UPDATE PROFILE =====")
                        print("1. Change Name")
                        print("2. Change Course")
                        print("3. Change Semester")
                        print("4. Back")

                        update = int(input("Enter your choice: "))

                        match update:

                            case 1:
                                print("Current Name :", name)
                                name = input("Enter New Name: ")
                                print("Name Updated Successfully")

                            case 2:
                                print("Current Course :", course)
                                course = input("Enter New Course: ")
                                print("Course Updated Successfully")

                            case 3:
                                print("Current Semester :", semester)
                                semester = int(input("Enter New Semester: "))
                                print("Semester Updated Successfully")

                            case 4:
                                break

                            case _:
                                print("Invalid Choice")

                case 7:
                    print("Logout Successfully")
                    break

                case _:
                    print("Invalid Choice")

    else:
        print("Invalid Login")