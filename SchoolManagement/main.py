from school.school import School

school = School("My School")

while True:

    print("\n" + "=" * 40)
    print("      SCHOOL MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1.  Add Student")
    print("2.  View All Students")
    print("3.  Search Student")
    print("4.  Update Student")
    print("5.  Delete Student")
    print("6.  Add Teacher")
    print("7.  View All Teachers")
    print("8.  Delete Teacher")
    print("9.  Take Attendance")
    print("10. Attendance Report")
    print("11. Pay Fee")
    print("12. Pending Fee List")
    print("13. Add Marks")
    print("14. Report Card")
    print("0.  Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        school.add_student()
    elif choice == "2":
        school.view_students()
    elif choice == "3":
        school.search_student()
    elif choice == "4":
        school.update_student()
    elif choice == "5":
        school.delete_student()
    elif choice == "6":
        school.add_teacher()
    elif choice == "7":
        school.view_teachers()
    elif choice == "8":
        school.delete_teacher()
    elif choice == "9":
        school.take_attendance()
    elif choice == "10":
        school.attendance_report()
    elif choice == "11":
        school.pay_fee()
    elif choice == "12":
        school.pending_fee_list()
    elif choice == "13":
        school.add_marks()
    elif choice == "14":
        school.report_card()
    elif choice == "0":
        print("Thank you! Goodbye.")
        break
    else:
        print("Invalid choice, try again.")
