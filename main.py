from newbook import add_book, create_base
from display_books import display_books
from search_book import search_book
from student_registration import registration, create_db
from issue_book import issued_book, create_dbase
from give_back import return_book
from delete_book import delete_book

# JSON files created
create_db()
create_base()
create_dbase()

while True:
    print("\n======== LIBRARY MANAGEMENT =======")
    print("1. Add new book")
    print("2. Display All books")
    print("3. Search for a book")
    print("4. Register a Student")
    print("5. Issue a book")
    print("6. Return a book")
    print("7. Delete a book")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number between 1 and 8")
        continue

    if choice == 1:
        add_book()
    elif choice == 2:
        display_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        registration()
    elif choice == 5:
        issued_book()
    elif choice == 6:
        return_book()
    elif choice == 7:
        delete_book()
    elif choice == 8:
        exit()
    else:
        print("Invalid choice")
