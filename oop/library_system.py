class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title=title, author=author)
        self.file_size = file_size
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title=title, author=author)
        self.page_count = page_count
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        if isinstance(book,Book):
            self.books.append(book)
            print(f'Added {book.title} to the library.')
        else:
            print("only instances of Book or its subclasses can be added.")
    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(f'- {book.title} by {book.author}')
                if isinstance(book, EBook):
                   print(f'  (E-Book, Size: {book.file_size}MB)')
                elif isinstance(book, PrintBook):
                   print(f'  (Print Book, Pages: {book.page_count})')
