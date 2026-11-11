import json
import os

def create_base():
    if not os.path.exists(BOOK_NAME):
        with open(BOOK_NAME, "w") as file:
            json.dump({}, file)
BOOK_NAME = "books.json"


# LOAD BOOKS
def load_books():
    with open(BOOK_NAME, "r") as file:
        books=json.load(file)

    return books

# SAVE BOOKS
def save_books(books):
    with open(BOOK_NAME, "w") as file:
        json.dump(books, file,indent=4)


# ADD BOOKS
def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Book already exists")
    else:
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        category = input("Enter Book Category: ")
        no_of_copy = int(input("Enter number of copies: "))
        if int(no_of_copy)<=0:
            print("Number of copies can't be zero or negative")
            return
        book={
            "book_id":book_id,
            "book_name":book_name,
            "author":author,
            "category":category,
            "available_copies":no_of_copy
        }
        books.append(book)
        save_books(books)
        print("Book registered")
