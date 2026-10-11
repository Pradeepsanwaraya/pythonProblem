subjects=frozenset(["Python","Java","MySQL","React","Spring Boot"])

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

while True:
    print("1. Display Subjects")
    print("2. Search Subject")
    print("3. Count Subjects")
    print("4. Attempt to Add Subject")
    print("5. Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        print(subjects)

    elif choice==2:
        subject=input("Enter Subject: ")
        if subject in subjects:
            print("Subject Found")
        else:
            print("Subject Not Found")

    elif choice==3:
        print(len(subjects))

    elif choice==4:
        subject=input("Enter Subject: ")
        try:
            subjects.add(subject)
        except AttributeError:
            print("Modification is not allowed in Frozen Set")

    elif choice==5:
        break

    else:
        print("Invalid Choice")