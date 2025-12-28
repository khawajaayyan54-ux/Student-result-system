student = {"ayyan":
           {"maths": 56,
            "english" : 78,
            "urdu" : 35,
            "physics" : 45,},
            
            "yousuf":
           {"maths": 56,
            "english" : 78,
            "urdu" : 35,
            "physics" : 45,},
            
            "sam":
           {"maths": 80,
            "english" : 78,
            "urdu" : 54,
            "physics" : 65,},
            
            "mick":
           {"maths": 35,
            "english" : 79,
            "urdu" : 97,
            "physics" : 34,},
            
            "jordan":
           {"maths": 28,
            "english" : 98,
            "urdu" : 38,
            "physics" : 84,},

            "liya":
           {"maths": 56,
            "english" : 78,
            "urdu" : 35,
            "physics" : 45,}}


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
