from classes.book import Book
from classes.user import User
from classes.library import Library
from classes.data import Data

library = Library()
d = Data()
d.write_json_book()
d.write_json_user()
d.read_json_book()
d.read_json_user()

choice = None
while choice != "7":
    print("1. Add Book\n2. Add User\n3. Borrow Book\n4.return_book\n5.list_available_books\n6.search_book\n7. Save & Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        titel = input("Enter the book name: ")
        author = input("Enter the author's name: ")
        ISBN = input("Enter the book's ID number: ")
        book = Book(titel,author,ISBN)
        library.add_book(book)
    
    elif choice == "2":
        naim = input("Enter your name: ")
        id = input("Enter your identification number: ")
        user = User(naim,id)        
        library.add_user(user)

    elif choice == "3":
        user_id =input("Enter your identification number: ")
        book_isbn = input("Enter the book's ID number: ")
        library.borrow_book(user_id,book_isbn)

    elif choice == "4":
        user_id =input("Enter your identification number: ")
        book_isbn = input("Enter the book's ID number: ")
        library.return_book(user_id,book_isbn)     
    
    elif choice == "5":
         library.list_available_books()

    elif choice == "6":
         title_or_author = input("Enter the name of the book or author: ")
         library.search_book(title_or_author)
             
    elif choice == "7":
            break
    else:
        print("Invalid choice, try again: ")