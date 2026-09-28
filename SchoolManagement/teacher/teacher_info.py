class Teacher:

    def __init__(self, teacher_id, name, subject, phone):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.phone = phone

    def display(self):
        print("ID      :", self.teacher_id)
        print("Name    :", self.name)
        print("Subject :", self.subject)
        print("Phone   :", self.phone)
