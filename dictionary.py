student_mark = {
    "swamesh rai": 95,
    "vibhu mishra": 89,
    "vats vartual singh": 91,
    "master bhayia": 33
}

student_name = input("Enter the student name: ")

if student_name in student_mark:
    print(f"{student_name}'s marks: {student_mark[student_name]}")
else:
    print("Student not found in the record.")


 


