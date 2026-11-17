from newbook import *


def search_book():
    books = load_books()

    if len(books) == 0:
        print("No books found")
        return

    keyword = input("Enter Book ID, Book Name or Author: ")

    if keyword == "":
        print("enter keyword ")
        return

    found = False
    for book in books:
        if keyword in book["book_id"] or keyword in book["book_name"] or keyword in book["author"]:
            found = True
            print("BOOK FOUNDED")
            print("\nBook Id:", book["book_id"])
            print("Book Name:", book["book_name"])
            print("Book Author:", book["author"])
            print("Category:", book["category"])
            print("Available copies:", book["available_copies"])   # FIX 3: "available copies" -> "available_copies"

    if found == False:
        print("No matching book found")
