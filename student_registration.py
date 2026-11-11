import json
import os


def create_db():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump({}, file)
FILE_NAME = "students.json"

#LOAD STUDENTS
def load_students():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


#SAVE STUDENTS
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file,indent=4)

#REGISTRATION
def registration():
    students=load_students()

    student_id=input("Enter Student ID: ")
    if student_id=="":
        print("Student ID is required")
        return
    if student_id in students:
        print("Student already exists")
    else:
        student_name=input("Enter Student Name: ")
        department=input("Enter Student Department: ")
        contact_number=input("Enter Student Contact Number: ")
        if student_name=="" or department=="":
            print("Student Name and Department are required")
            return
        if len(contact_number)!=10:
            print("contact number requires 10 digits")
            return

        student={"student_id":student_id,
                 "student_name":student_name,
                 "department":department,
                 "contact_number":contact_number}
        students.append(student)
        save_students(students)
        print("Student registered")



