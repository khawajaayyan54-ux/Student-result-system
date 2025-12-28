student = {}

with open("student.txt","r") as file:
    for line in file:
        parts = line.strip().split(",")
        name = parts[0]
        student[name] = {}
        for item in parts[1:]:
            subject, mark = item.split("=")
            student[name][subject] = int(mark)

def code():
    user = input("Enter the student name: ").lower()
    if user == "all name":
        print("STUDENT NAME: ")
        for st_name, st_data in student.items():
            print(st_name.capitalize())
    
    elif user == "all details":
        for st_name, st_data in student.items():
            print(f"{st_name.capitalize()}: ")
            for subject, mark in st_data.items():
                print(f"{subject.capitalize()} : {mark}")
            print()

    else:        
        if user in student:
            total = 0
            for marks in student[user].values():
                total += marks
            percentage = total/400*100
            print("SUBJECT AND MARKS: ")
            for subject, mark in student[user].items():
                print(f"{subject.capitalize()} : {mark}")
            
            if percentage >= 80:
                grade = "A+"
            elif percentage >= 70:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 40:
                grade = "C"
            else:
                grade = "F"
            print("STUDENT DETAILS: ")    
            if percentage >= 40:
                print(f"Name : {user.capitalize()}\nTotal Marks : {total}\nStatus : Passed\nPercentage: {percentage}%\nGrade : {grade}")
            else:
                print(f"Name : {user.capitalize()}\nTotal Marks : {total}\nStatus : Failed\nPercentage: {percentage}%\nGrade : {grade}")

        else:
            print("user not found")

code()

while True:
    startcode = input("Type y to continue(y/n): ")
    if startcode == "y":
        code()
    elif startcode == "n":
        break
    else:
        print("error smth went wrong")    
