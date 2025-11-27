students = []


# add student
def add_student(students):
    name = input("Add students name:")
    for student in students:
        if student["name"] == name:
            print("Student already exists!")
            return

    new_student = {"name": name, "grades": []}
    students.append(new_student)


def add_grade(students):
    needed_student = input("What student do you need? ")
    #check if student exists
    for student in students:
        if needed_student == student["name"]:
            while True:
                student_grade = input("Input grades: ")
                if student_grade == "done":
                    break

                try:
                    student["grades"].append(int(student_grade))
                except ValueError:
                    print("Invalid input! Please enter a number")
            return
    print("Student not found")


def show_report(students):
    if len(students) == 0:
        print("No students added yet!")
        return
        # list to save averages
    all_averages = []

    for student in students:
        try:
            if student["grades"] and len(student["grades"]) > 0:
                average_num = sum(student["grades"]) / len(student["grades"])
                all_averages.append(average_num)
                print(f"{student['name']}'s average grade is {average_num:.2f}")
            else:
                print(f"{student['name']}'s average grade is N/A")
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A")

    # summary
    if len(all_averages) > 0:
        print("\n----------------")
        print(f"Max average: {max(all_averages):.2f}")
        print(f"Min average: {min(all_averages):.2f}")
        print(f"Overall average: {sum(all_averages) / len(all_averages):.2f}")
    else:
        print("\nNo grades have been added yet!")


def find_top_performer(students):
    # check
    if len(students) == 0:
        print("No students added!")
        return

    # filter
    students_with_grades = [
        student
        for student in students
        if student["grades"] and len(student["grades"]) > 0
    ]

    if len(students_with_grades) == 0:
        print("No students with grades yet!")
        return

    # top student
    top_student = max(
        students_with_grades,
        key=lambda student: sum(student["grades"]) / len(student["grades"]),
    )

    average = sum(top_student["grades"]) / len(top_student["grades"])
    print(f"Top student is {top_student['name']} with average: {average:.2f}")


def main():
    while True:
        try:
            print("\n--- Student Grade Analyzer ---")
            print("1. Add a new student")
            print("2. Add grades for student")
            print("3. Show report (all students)")
            print("4. Find top performer")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                add_student(students)
            elif choice == "2":
                add_grade(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                find_top_performer(students)
            elif choice == "5":
                print("Exiting ")
                break
            else:
                print("Invalid choice! Please enter 1-5.")

        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")


main()
