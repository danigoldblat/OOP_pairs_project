from classes.book import Book
from classes.user import User

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []
    def __str__(self):
        return f"list_of_books: {self.list_of_books} list_of_users: {self.list_of_users }"
    

    def add_book(self,book):
        self.list_of_books.append(book)


    def add_user(self,user):
        self.list_of_users.append(user)


    def borrow_book(self,user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN == book_isbn:
                if book.is_available == True:
                    book.is_available = False
                    for user in self.list_of_users:
                        if user.id == user_id:
                            user.borrowed_books.append(book)
                            return f"You asked for the book.: {book_isbn} successfully"
                        else:
                             return "Does not identify user as"
            else:
                return "The book is not available."
    
                 


    def return_book(self,user_id, book_isbn):
        for book in self.list_of_books:
            if book.ISBN == book_isbn:
                if book.is_available == False:
                    book.is_available = True
                    for user in self.list_of_users:
                        if user.id == user_id:
                            user.borrowed_books.remove(book)
            
                return "The book is already available."
            
            else:
                return "Does not identify user as" 



    def list_available_books(self):
        temporary_books = []
        for book in self.list_of_books:
            if book.is_available == True:
                temporary_books.append(book)
        return temporary_books


    def search_book(self,title_or_author):
        for i in  self.list_of_books:
            if i == title_or_author:
                return True