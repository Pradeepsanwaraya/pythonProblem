class Student:

    def __init__(self, roll_no, name, student_class, phone, parent_name, total_fee):
        self.roll_no = roll_no
        self.name = name
        self.student_class = student_class
        self.phone = phone
        self.parent_name = parent_name
        self.total_fee = total_fee
        self.fee_paid = 0
        self.marks = {}            # {"Maths": 80, "English": 70}
        self.present_days = 0
        self.total_days = 0

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def pay_fee(self, amount):
        self.fee_paid = self.fee_paid + amount

    def pending_fee(self):
        return self.total_fee - self.fee_paid

    def mark_attendance(self, is_present):
        self.total_days = self.total_days + 1
        if is_present:
            self.present_days = self.present_days + 1

    def attendance_percent(self):
        if self.total_days == 0:
            return 0
        return round(self.present_days * 100 / self.total_days, 1)

    def display(self):
        print("Roll No     :", self.roll_no)
        print("Name        :", self.name)
        print("Class       :", self.student_class)
        print("Phone       :", self.phone)
        print("Parent Name :", self.parent_name)
        print("Total Fee   :", self.total_fee)
        print("Fee Paid    :", self.fee_paid)
        print("Pending Fee :", self.pending_fee())
        print("Attendance  :", self.attendance_percent(), "%")
