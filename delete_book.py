from newbook import load_books, save_books
from issue_book import load_issue_books

def delete_book():
    books=load_books()
    issued=load_issue_books()

    book_id=input("Enter the book id to delete")

    for book in books:
        if book["book_id"]==book_id:
            selected_book=book
            print("book founded")
    for record in issued:
        if record["book_id"]==book_id:
            print("book is issued now")

    books.remove(selected_book)
    save_books(books)

    print("book deleted")
