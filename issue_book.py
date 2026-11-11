import json
import os
import datetime
from newbook import load_books, save_books
from student_registration import load_students


def create_dbase():
    if not os.path.exists(ISSUE_BOOK):
        with open(ISSUE_BOOK, "w") as file:
            json.dump({}, file)
ISSUE_BOOK="issued_books.json"

# LOAD ISSUE BOOKS
def load_issue_books():
    with open(ISSUE_BOOK, "r") as file:
        issues= json.load(file)
    return issues
# SAVE ISSUED BOOKS
def issued_books(issues):
    with open(ISSUE_BOOK, "w") as file:
        json.dump(issues, file,indent=4)

def issued_book():
    books = load_books()
    students = load_students()
    issued = load_issue_books()

    student_id=input("Enter Student ID:")
    book_id=input("Enter Book ID:")
    for student in students:
        if student["student_id"] == student_id:
            for book in books:
                if book["book_id"] == book_id:
                    selected_book=book
                    if selected_book["available_copies"] ==0:
                        print("No copy available")
                        return
                    else:
                        selected_book["available_copies"] = selected_book["available_copies"]-1
                        save_books(books)
    record={
        "student_id":student_id,
        "book_id":book_id,
        "issue_date": str(datetime.datetime.today()),
    }
    issued.append(record)
    issued_books(issued)

    print("Issued book added")