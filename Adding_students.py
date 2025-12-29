import os
import json
Filename = "students.json"
if os.path.exists(Filename):
    with open(Filename, "r") as f:
        students = json.load(f)

else:
    students = {}

def adding_students():
    name = input("Enter student's name: ").lower().strip()
    if not name:
        print("please type student name")
        return
    
    if not name.replace(" ", "").isalpha():
        print("Name must contain letters only")
        return
    
    subjects = ["maths","science","physics","english"]
    marks = {}
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100")
            except ValueError:
                print("Please enter the valid number")
    
    students[name] = marks

    with open(Filename, "w") as f:
        json.dump(students,f,indent=4)
    print(f"{name} has been added to the list")

while True:
    adding_students()
    start = input("type y to continue and n to stop: ")
    if start != "y":
        print("exiting program: ")
        break