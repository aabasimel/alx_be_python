class Book:
    """A class representing a book in the library system."""
    
    def __init__(self, title, author):
        """Initialize a book with title, author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Check out the book if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Return the book to make it available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize a library with an empty list of books."""
        self._books = []  # Private list to store book instances
    
    def add_book(self, book):
        """Add a book to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only Book objects can be added to the library")
    
    def check_out_book(self, title):
        """
        Check out a book by title.
        Returns True if successful, False if book not found or already checked out.
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False
    
    def return_book(self, title):
        """
        Return a book by title.
        Returns True if successful, False if book not found or not checked out.
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False
    
    def list_available_books(self):
        """List all books that are currently available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books available in the library.")
        else:
            for book in available_books:
                print(book)
    
    def find_book(self, title):
        """Find a book by title (case-insensitive)."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def get_total_books(self):
        """Get the total number of books in the library."""
        return len(self._books)
    
    def get_checked_out_books(self):
        """Get list of books that are currently checked out."""
        return [book for book in self._books if not book.is_available()]