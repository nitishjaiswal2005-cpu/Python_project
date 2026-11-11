from newbook import *

def display_books():
    books=load_books()

    if len(books)==0:
        print("Library doesn't have any books")
        return

    for book in books:
        print("\nBook ID:",book["book_id"])
        print("Book Name:",book["book_name"])
        print("Book Author:",book["author"])
        print("Category:",book["category"])
        print("Available copies:",book["available copies"])