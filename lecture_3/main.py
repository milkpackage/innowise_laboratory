students = []


# add student
def add_student(students):
    name = input("Add students name:")
    for student in students:
        if student["name"] == name:
            print("Student already exists!")
    else:
        new_student = {"name": name, "grades": None}
        students.append(new_student)


def add_grade(students):
    needed_student = input("What student do you need? ")
    for student in students:
        if needed_student == student["name"]:
            if student["grades"] == None:
                student["grades"] = []

            while True:
                student_grade = input("Input grades: ")
                if student_grade == "done":
                    break
                student["grades"].append(int(student_grade))
                print(student)
            break


def show_report(students):
    for student in students:
        if len(student["grades"]) != 0:
            average_num = sum(student["grades"]) / len(student["grades"])
            student_name = student["name"]
            print(f"{student_name}'s average grade is {average_num}")
        else:
            student_name = student["name"]
            grade = student["grades"]
            grade = "N/A"
            print(f"{student_name}'s average grade is {grade}")


def main():
    while True:
        print("1. Add a new student")
        print("2. Add grades for student")
        print("3. Show report(all students)")
        print("4. Find top performer")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student(students)
            print(students)
        elif choice == "2":
            add_grade(students)
        elif choice == "3":
            show_report(students)
        else:
            break


main()
