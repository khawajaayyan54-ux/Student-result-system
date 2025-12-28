## Student Marks System

This is a Python program that allows users to view marks of students in multiple subjects. It calculates total marks, percentage, pass/fail status, and grades for each student.

## Features

. View subject-wise marks for any student
. View all student names
. View all students’ details
. Calculates total marks
. Calculates percentage dynamically based on the number of subjects
. Determines pass/fail status
. Assigns grades based on percentage
. Handles errors like missing files or invalid data

## How to Run

1. Clone the repository or download the code.

2. Make sure student.txt exists in the same folder with correct formatting:
. ayyan,maths=56,english=78,urdu=35,physics=45
  sam,maths=65,english=75,physics=87,chemistry=53


3. Run the Python file:
. python project.py

4. Enter a student name, or use commands:
. all name – lists all students
. all details – lists all students with their subject-wise marks

5. Type 'y' to continue or 'n' to exit after each query.

## Example Output
Name: Ayyan
Subjects & Marks:
Maths: 56
English: 78
Urdu: 35
Physics: 45
Total Marks: 214
Percentage: 53.50%
Status: Passed
Grade: C

## Precautions

. Ensure student.txt exists and follows the correct format.
. All marks must be numbers; invalid entries will be ignored.
. Missing subjects will reduce the total count and affect percentage calculation.
. The program will not crash on file or data errors but will show a warning.
