
def details():
    name=input("enter name of student")
    rollno=int(input("enter name of rollno"))

    marks1=int(input("enter marks of subject1: "))
    marks2=int(input("enter marks of subject2: "))
    marks3=int(input("enter marks of subject3: "))
    marks4=int(input("enter marks of subject4: "))
    marks5=int(input("enter marks of subject5: "))

    return name,rollno,marks1,marks2,marks3,marks4,marks5


def total(marks1,marks2,marks3,marks4,marks5):
    totalmarks=marks1+marks2+marks3+marks4+marks5
    return totalmarks


def percentage(totalmarks):
    per=totalmarks/5
    return per


def grade(per):
    if per>=90:
        return "Grade A+"
    elif per>=80:
        return "Grade A"
    elif per>=70:
        return "Grade B"
    elif per>=60:
        return "Grade C"
    elif per>=50:
        return "Grade D"
    else:
        return "Fail"


def highest(marks1,marks2,marks3,marks4,marks5):
    high=marks1

    if marks2>high:
        high=marks2
    if marks3>high:
        high=marks3
    if marks4>high:
        high=marks4
    if marks5>high:
        high=marks5

    return high


def lowest(marks1,marks2,marks3,marks4,marks5):
    low=marks1

    if marks2<low:
        low=marks2
    if marks3<low:
        low=marks3
    if marks4<low:
        low=marks4
    if marks5<low:
        low=marks5

    return low


while True:
    print("\nstudent result management")
    print("1. add student details")
    print("2. calculate total marks")
    print("3. calculate percentage")
    print("4. find grade")
    print("5. display complete result")
    print("6. find highest subject mark")
    print("7. find lowest subject mark")
    print("8. exit")

    choice=int(input("enter choice : "))

    match choice:

        case 1:
            name,rollno,marks1,marks2,marks3,marks4,marks5=details()
            print("student details added successfully")

        case 2:
            totalmarks=total(marks1,marks2,marks3,marks4,marks5)
            print("total marks =",totalmarks)

        case 3:
            totalmarks=total(marks1,marks2,marks3,marks4,marks5)
            per=percentage(totalmarks)
            print("percentage =",per)

        case 4:
            totalmarks=total(marks1,marks2,marks3,marks4,marks5)
            per=percentage(totalmarks)
            print(grade(per))

        case 5:
            totalmarks=total(marks1,marks2,marks3,marks4,marks5)
            per=percentage(totalmarks)
            gr=grade(per)
            high=highest(marks1,marks2,marks3,marks4,marks5)
            low=lowest(marks1,marks2,marks3,marks4,marks5)

            print("\nresult card")
            print("name :",name)
            print("roll number :",rollno)
            print("subject 1 :",marks1)
            print("subject 2 :",marks2)
            print("subject 3 :",marks3)
            print("subject 4 :",marks4)
            print("subject 5 :",marks5)
            print("total marks :",totalmarks)
            print("percentage :",per)
            print("grade :",gr)
            print("highest mark :",high)
            print("lowest mark :",low)

        case 6:
            high=highest(marks1,marks2,marks3,marks4,marks5)
            print("highest mark =",high)

        case 7:
            low=lowest(marks1,marks2,marks3,marks4,marks5)
            print("lowest mark =",low)

        case 8:
            print("thank you. program terminated")
            break

        case _:
            print("invalid choice")
