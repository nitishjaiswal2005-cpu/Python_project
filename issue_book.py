import json
import os
import datetime
from newbook import load_books, save_books
from student_registration import load_students

ISSUE_BOOK = "issued_books.json"


def create_dbase():
    if not os.path.exists(ISSUE_BOOK):
        with open(ISSUE_BOOK, "w") as file:
            json.dump([], file)


# LOAD ISSUE BOOKS
def load_issue_books():
    with open(ISSUE_BOOK, "r") as file:
        issues = json.load(file)
    return issues


# SAVE ISSUED BOOKS
def issued_books(issues):
    with open(ISSUE_BOOK, "w") as file:
        json.dump(issues, file, indent=4)


def issued_book():
    books = load_books()
    students = load_students()
    issued = load_issue_books()

    student_id = input("Enter Student ID: ").strip().lower()
    book_id = input("Enter Book ID: ").strip().lower()

    #CHECKING STUDENT IS REGISTERED OR NOT
    student_found = False
    for student in students:
        if student["student_id"] == student_id:
            student_found = True

    if student_found == False:
        print("Student not found")
        return

    #CHECKING BOOK AVAILABILITY
    book_found = False
    for book in books:
        if book["book_id"] == book_id:
            book_found = True
            if book["available_copies"] == 0:
                print("No copy available")
                return
            book["available_copies"] = book["available_copies"] - 1
            save_books(books)

    if book_found == False:
        print("Book not found")
        return

    record = {
        "student_id": student_id,
        "book_id": book_id,
        "issue_date": str(datetime.datetime.today()),
    }
    issued.append(record)
    issued_books(issued)

    print("Issued book added")
