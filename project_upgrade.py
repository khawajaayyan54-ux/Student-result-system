
def load_students(filename):
    students = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                name = parts[0]
                students[name] = {}

                for item in parts[1:]:
                    subject, mark = item.split("=")
                    students[name][subject] = int(mark)

    except FileNotFoundError:
        print("Error: file not found. Please create student.txt first.")
    except Exception as e:
        print("Error reading file:", e)

    return students

def show_student_name(students):
    print("STUDENT NAME: ")
    for name in students:
        print(name.capitalize())

def show_student_details(students):
     for name, subjects in students.items():
        print(f"{name.capitalize()}:")
        for subject, mark in subjects.items():
            print(f"{subject.capitalize()} : {mark}")
        print()

def show_student_result(students, user):
        total = sum(students[user].values())
        percentage = total/(len(students[user])*100)*100

        print("SUBJECT AND MARKS: ")
        for subject, mark in students[user].items():
            print(f"{subject.capitalize()} : {mark}")
        print()
                       
        if percentage >= 80:
            grade = "A+"
        elif percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        status = "passed" if percentage >= 40 else "failed"
        print(f"Name : {user.capitalize()}\nTotal Marks : {total}\nStatus : {status}\nPercentage: {percentage}%\nGrade : {grade}")
def main(students):
    print("MENU: \n1. All Name\n2. All details\n3. Student name:")

    user = input("enter ur command or student name: ").lower()

    if user == "all name":
        show_student_name(students)
    elif user == "all details":
        show_student_details(students)
    elif user in students:
        show_student_result(students, user)
    else:
        print("user not found")

students = load_students("student.txt")


while True:
    main(students)
    startcode = input("Type y to continue(y/n): ")
    if startcode == "n":
        break