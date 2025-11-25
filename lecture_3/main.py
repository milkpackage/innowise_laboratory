students = [{"name" : "Bobby", "grades": 20},{"name" : "Adolf", "grades": None}]

#add student
def add_student():
   name = input('Add students name:')
   for student in students:
       if student["name"] == name:        
        print('Student already exists!')
   else:
       new_student = {"name" : name, "grades": None}
       students.append(new_student)

def add_grade(students):
    needed_student = input('What student do you need? ')
    for student in students:
        if needed_student == student["name"]:
            while True:
                student_grade = input('Input his grades:')
                if student_grade == "done":
                    break
                else:
                    print(students)
                    student["grades"].append(student_grade)
        


add_student()
print(students)
add_grade(students)
