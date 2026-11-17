from newbook import load_books, save_books
from issue_book import load_issue_books


def delete_book():
    books = load_books()
    issued = load_issue_books()

    book_id = input("Enter the book id to delete: ")

    found = False
    for book in books:
        if book["book_id"] == book_id:
            found = True
            selected_book = book

    #BOOK NOT FOUND
    if found == False:
        print("Book not found")
        return

    #ISSUED BOOK NOT DELETE
    for record in issued:
        if record["book_id"] == book_id:
            print("Book is currently issued, can't delete")
            return

    books.remove(selected_book)
    save_books(books)

    print("Book deleted")
