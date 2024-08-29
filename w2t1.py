students = []
def add_student(students):
    name = input("Enter the name of student : ")
    students.append(name)
    print(f"{name} added successfully.")

def remove_student(students):
    name = input("Enter the name of student to remove : ")
    if name in students:
        students.remove(name)
        print(f"{name} removed successfully.")
    else:
        print(f"{name} not found.")

def display_students(students):
    if not students:
        print("No students found.")
        return
    for student in students:
        print(student)

while True:
    
    print("1. Add student \n2. Remove student \n3. Display students \n4. Quit")
    choice = int(input("Choose choice : "))

    if choice == 1:
        add_student(students)
    elif choice == 2:
        remove_student(students)
    elif choice == 3:
        display_students(students)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")