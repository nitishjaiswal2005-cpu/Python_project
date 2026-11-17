from newbook import load_books, save_books
from issue_book import load_issue_books, issued_books


def return_book():
    books = load_books()
    issued = load_issue_books()

    student_id = input("Enter student ID: ")
    book_id = input("Enter book ID: ")

    found = False
    for record in issued:
        if record["student_id"] == student_id and record["book_id"] == book_id:
            found = True
            selected_record = record

            for book in books:
                if book["book_id"] == book_id:
                    book["available_copies"] = book["available_copies"] + 1

            save_books(books)
            break

    # RECORD NOT FOUND
    if found == False:
        print("No such issued record found")
        return

    issued.remove(selected_record)
    issued_books(issued)

    print("Issued book is returned")
