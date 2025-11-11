from classes.book import Book
from classes.user import User
from classes.library import Library

import json
class Data:
    def write_json_book(self):
        with open("books.json","w") as f:
            list_book = []
            l = Library()
            for i in l.list_of_books:
                list_book.append(i.__dict__)
            content_str = json.dumps(list_book)
            f.write(content_str)
            return l

            
    def read_json_book(self):
        with open("books.json","r") as f:
            list_book = []
            l = Library()
            for i in l.list_of_books:
                list_book.append(i.__dict__)
            content_str = json.loads(list_book)
            f.write(content_str)
            return l
    def write_json_user(self):
        with open("users.json","w") as f:
            list_user = []
            l = Library()
            for i in l.list_of_books:
                list_user.append(i.__dict__)
            content_str = json.dumps(list_user)
            f.write(content_str)
            return l

    def read_json_user(self):
        with open("users.json","w") as f:
            list_user = []
            l = Library()
            for i in l.list_of_books:
                list_user.append(i.__dict__)
            content_str = json.loads(list_user)
            f.write(content_str)
            return l