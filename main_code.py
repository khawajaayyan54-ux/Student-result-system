student = {"ayyan":
           {"maths": 56,
            "english" : 78,
            "urdu" : 35,
            "physics" : 45,},
            
            "Yousuf":
           {"maths": 56,
            "english" : 78,
            "urdu" : 35,
            "physics" : 45,},

            "liya":
           {"maths": 56,
            "english" : 78,
            "urdu" : 35,
            "physics" : 45,}}


def code():
    user = input("Enter the student name: ").lower()
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
            print(f"Name : {user}\nTotal Marks : {total}\nStatus : Passed\nPercentage: {percentage}%\nGrade : {grade}")
        else:
            print(f"Name : {user}\nTotal Marks : {total}\nStatus : Failed\nPercentage: {percentage}%\nGrade : {grade}")

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