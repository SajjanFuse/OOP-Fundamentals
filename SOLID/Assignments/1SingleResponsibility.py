"""
[Single-Responsibility Principle (SRP)] 
Implement a simple program to interact with the library catalog system. 
Create a Python class Book to represent a single book with attributes: Title, Author, ISBN, Genre, Availability (whether the book is available for borrowing or not). 
Create another Python class LibraryCatalog to manage the collection of books with following functionalities:
Add books by storing each book objects (Hint: Create an empty list in constructor and store book objects)
get book details and get all books from the list of objects
Lets say, we need a book borrowing process (what books are borrowed and what books are available for borrowing). 
Implement logics to integrate this requirement in the above system. 
Design the classes with a clear focus on adhering to the Single Responsibility Principle(SRP) which represents that "A module should be responsible to one, and only one, actor."

"""
import logging 

logging.basicConfig(filename='bookManagement.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Book:
    def __init__(self, title, author, ISBN, Genre, Availability=True):
        self.title = title 
        self.author = author 
        self.isbn = ISBN
        self.genre = Genre 
        self.availability = Availability

    
class LibraryCatalog:
    def __init__(self):
        self.bookList = [] 

    def addBook(self, book):
        self.bookList.append(book)


    def get_book_details(self, isbn):
        for book in self.bookList:
            if book.isbn == isbn:
                return book
        # no book found with matching ISBN
        return None

    def get_all_books(self):
        return self.bookList

    def borrow_book(self, isbn):
        for book in self.bookList:
            if book.isbn == isbn:
                if book.availability:
                    book.availability = False
                    logging.info(f"Book '{book.title}' has been borrowed.")
                else:
                    logging.warning(f"Book '{book.title}' is not available for borrowing.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.bookList:
            if book.isbn == isbn:
                book.availability = True
                logging.info(f"Book '{book.title}' has been returned.")
                return
        logging.warning(f"Book with isbn {isbn} not found.")

# Example usage
if __name__ == "__main__":
    catalog = LibraryCatalog()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Fiction")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Fiction")
    book3 = Book("1984", "George Orwell", "9780451524935", "Dystopian Fiction")

    catalog.addBook(book1)
    catalog.addBook(book2)
    catalog.addBook(book3)

    print("All Books:")
    for book in catalog.get_all_books():
        print(book)

    print("\nBorrowing a Book:")
    catalog.borrow_book("9780743273565")
    catalog.borrow_book("9780451524935")
    catalog.borrow_book("123456789")  # Non-existent 
    catalog.borrow_book("9780743273565")

    print("\nReturning a Book:")
    catalog.return_book("9780743273565")
    catalog.return_book("123456789")  # Non-existent book

