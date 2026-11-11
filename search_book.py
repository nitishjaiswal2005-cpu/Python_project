import keyword

from newbook import *

def search_book():
    books=load_books()

    if len(books)==0:
        print("No books found")
        return

    keyword=input("Enter Book ID,Book Name:")

    if keyword=="":
        print("enter keyword ")
        return
    else:
        for book in books:
            if keyword in book["book_id"] or keyword in book["book_name"] or keyword in book["author"]:
                print("BOOK FOUNDED")
                print("\nBook Id:",book["book_id"])
                print("Book Name:",book["book_name"])
                print("Book Author:",book["author"])
                print("Category:",book["category"])
                print("Available copies:",book["available copies"])


