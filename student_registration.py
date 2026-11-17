import json
import os

FILE_NAME = "students.json"


def create_db():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)      # FIX 1: {} ki jagah [] (list)


# LOAD STUDENTS
def load_students():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


# SAVE STUDENTS
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# REGISTRATION
def registration():
    students = load_students()

    student_id = input("Enter Student ID: ").strip().lower()
    if student_id == "":
        print("Student ID is required")
        return

    # COMPARE STUDENT ID
    for student in students:
        if student["student_id"] == student_id:
            print("Student already exists")
            return

    student_name = input("Enter Student Name: ").strip()
    department = input("Enter Student Department: ").strip()
    contact_number = input("Enter Student Contact Number: ").strip()
    if student_name == "" or department == "":
        print("Student Name and Department are required")
        return
    if len(contact_number) != 10:
        print("contact number requires 10 digits")
        return

    student = {"student_id": student_id,
               "student_name": student_name,
               "department": department,
               "contact_number": contact_number}
    students.append(student)
    save_students(students)
    print("Student registered")
