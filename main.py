from classes.book import Book
from classes.user import User
from classes.library import Library

book = Book("Finance","yossi",554)
user = User("avi",77896)
library = Library()
library.add_book(book)
library.add_user(user)
print(library)
print(library.borrow_book(77896,554))