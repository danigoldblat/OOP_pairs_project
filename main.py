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




choice = None
while choice != "7":
    print("1. Add Book\n2. Add User\n3. Borrow Book\n7. Save & Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        titel = input("Enter the book name")
        author = input("Enter the author's name")
        ISBN = input("Enter the book's ID number.")
        book = Book(titel,author,ISBN)
        library.add_book(book)
    
    elif choice == "2":
        naim = input("Enter your name")
        id = input("Enter your identification number")
        user = User(naim,id)        
        library.add_user(user)
    elif choice == "7":
# save data and exit
            break
    else:
        print("Invalid choice, try again.")