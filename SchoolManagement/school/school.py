from student.student_info import Student
from teacher.teacher_info import Teacher
from utils.validation import validate_name, validate_phone, get_number


class School:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    # ================= STUDENT =================

    def find_student(self, roll_no, student_class):
        for s in self.students:
            if s.roll_no == roll_no and s.student_class == student_class:
                return s
        return None

    def ask_student(self):
        """Ask for class + roll no and return that student (or None)."""
        student_class = input("Enter class: ").strip()
        roll_no = input("Enter roll no: ").strip()
        student = self.find_student(roll_no, student_class)
        if student is None:
            print("Student not found!")
        return student

    def add_student(self):
        print("\n========== ADD STUDENT ==========")
        student_class = input("Enter class: ").strip()
        roll_no = input("Enter roll no: ").strip()

        if student_class == "" or roll_no == "":
            print("Class and roll no are required!")
            return

        if self.find_student(roll_no, student_class):
            print("This roll no already exists in this class!")
            return

        name = input("Enter student name: ").strip()
        if not validate_name(name):
            print("Invalid name! Use letters only.")
            return

        phone = input("Enter phone (10 digits): ").strip()
        if not validate_phone(phone):
            print("Invalid phone number!")
            return

        parent_name = input("Enter parent name: ").strip()
        total_fee = get_number("Enter total fee: ")

        self.students.append(Student(roll_no, name, student_class, phone, parent_name, total_fee))
        print("Student added successfully!")

    def view_students(self):
        print("\n========== ALL STUDENTS ==========")
        if len(self.students) == 0:
            print("No students yet.")
            return
        for s in self.students:
            print("-" * 30)
            s.display()

    def search_student(self):
        print("\n========== SEARCH STUDENT ==========")
        text = input("Enter name to search: ").strip().lower()
        found = False
        for s in self.students:
            if text in s.name.lower():
                print("-" * 30)
                s.display()
                found = True
        if not found:
            print("No student found!")

    def update_student(self):
        print("\n========== UPDATE STUDENT ==========")
        student = self.ask_student()
        if student is None:
            return

        print("1. Name")
        print("2. Phone")
        print("3. Parent Name")
        print("4. Total Fee")
        choice = input("What do you want to update? ")

        if choice == "1":
            name = input("Enter new name: ").strip()
            if validate_name(name):
                student.name = name
            else:
                print("Invalid name!")
                return
        elif choice == "2":
            phone = input("Enter new phone: ").strip()
            if validate_phone(phone):
                student.phone = phone
            else:
                print("Invalid phone number!")
                return
        elif choice == "3":
            student.parent_name = input("Enter new parent name: ").strip()
        elif choice == "4":
            student.total_fee = get_number("Enter new total fee: ")
        else:
            print("Invalid choice")
            return
        print("Student updated successfully!")

    def delete_student(self):
        print("\n========== DELETE STUDENT ==========")
        student = self.ask_student()
        if student is None:
            return
        sure = input(f"Delete {student.name}? (yes/no): ")
        if sure.lower() == "yes":
            self.students.remove(student)
            print("Student deleted.")

    # ================= TEACHER =================

    def add_teacher(self):
        print("\n========== ADD TEACHER ==========")
        teacher_id = input("Enter teacher ID: ").strip()

        for t in self.teachers:
            if t.teacher_id == teacher_id:
                print("This teacher ID already exists!")
                return

        name = input("Enter teacher name: ").strip()
        if not validate_name(name):
            print("Invalid name! Use letters only.")
            return

        subject = input("Enter subject: ").strip()
        phone = input("Enter phone (10 digits): ").strip()
        if not validate_phone(phone):
            print("Invalid phone number!")
            return

        self.teachers.append(Teacher(teacher_id, name, subject, phone))
        print("Teacher added successfully!")

    def view_teachers(self):
        print("\n========== ALL TEACHERS ==========")
        if len(self.teachers) == 0:
            print("No teachers yet.")
            return
        for t in self.teachers:
            print("-" * 30)
            t.display()

    def delete_teacher(self):
        print("\n========== DELETE TEACHER ==========")
        teacher_id = input("Enter teacher ID: ").strip()
        for t in self.teachers:
            if t.teacher_id == teacher_id:
                self.teachers.remove(t)
                print("Teacher deleted.")
                return
        print("Teacher not found!")

    # ================= ATTENDANCE =================

    def take_attendance(self):
        print("\n========== TAKE ATTENDANCE ==========")
        student_class = input("Enter class: ").strip()

        class_students = [s for s in self.students if s.student_class == student_class]
        if len(class_students) == 0:
            print("No students in this class!")
            return

        for s in class_students:
            while True:
                status = input(f"{s.roll_no} - {s.name} (p = present, a = absent): ").lower()
                if status == "p":
                    s.mark_attendance(True)
                    break
                elif status == "a":
                    s.mark_attendance(False)
                    break
                else:
                    print("Enter only p or a")
        print("Attendance saved!")

    def attendance_report(self):
        print("\n========== ATTENDANCE REPORT ==========")
        student_class = input("Enter class: ").strip()
        found = False
        print(f"{'Roll':<8}{'Name':<20}{'Present':<10}{'Total':<8}{'%'}")
        for s in self.students:
            if s.student_class == student_class:
                print(f"{s.roll_no:<8}{s.name:<20}{s.present_days:<10}{s.total_days:<8}{s.attendance_percent()}")
                found = True
        if not found:
            print("No students in this class!")

    # ================= FEES =================

    def pay_fee(self):
        print("\n========== PAY FEE ==========")
        student = self.ask_student()
        if student is None:
            return

        print("Pending fee:", student.pending_fee())
        amount = get_number("Enter amount to pay: ")

        if amount > student.pending_fee():
            print("Amount is more than pending fee!")
            return

        student.pay_fee(amount)
        print("Payment successful! Pending fee now:", student.pending_fee())

    def pending_fee_list(self):
        print("\n========== PENDING FEES ==========")
        found = False
        for s in self.students:
            if s.pending_fee() > 0:
                print(f"Class {s.student_class} | Roll {s.roll_no} | {s.name} | Pending: {s.pending_fee()}")
                found = True
        if not found:
            print("No pending fees.")

    # ================= MARKS =================

    def add_marks(self):
        print("\n========== ADD MARKS ==========")
        student = self.ask_student()
        if student is None:
            return

        subject = input("Enter subject: ").strip()
        marks = get_number("Enter marks (out of 100): ")
        if marks > 100:
            print("Marks cannot be more than 100!")
            return

        student.add_marks(subject, marks)
        print("Marks saved!")

    def report_card(self):
        print("\n========== REPORT CARD ==========")
        student = self.ask_student()
        if student is None:
            return

        if len(student.marks) == 0:
            print("No marks added for this student.")
            return

        print("\n" + "=" * 40)
        print(self.name.upper().center(40))
        print("REPORT CARD".center(40))
        print("=" * 40)
        print("Name  :", student.name)
        print("Class :", student.student_class, "  Roll No:", student.roll_no)
        print("-" * 40)
        print(f"{'Subject':<25}{'Marks'}")

        total = 0
        failed = False
        for subject, marks in student.marks.items():
            print(f"{subject:<25}{marks}")
            total = total + marks
            if marks < 33:
                failed = True

        percent = round(total / (len(student.marks) * 100) * 100, 2)

        if percent >= 90:
            grade = "A+"
        elif percent >= 80:
            grade = "A"
        elif percent >= 70:
            grade = "B+"
        elif percent >= 60:
            grade = "B"
        elif percent >= 50:
            grade = "C"
        elif percent >= 40:
            grade = "D"
        else:
            grade = "F"

        print("-" * 40)
        print("Total      :", total, "/", len(student.marks) * 100)
        print("Percentage :", percent, "%")
        print("Grade      :", grade)
        print("Result     :", "FAIL" if failed else "PASS")
        print("=" * 40)
