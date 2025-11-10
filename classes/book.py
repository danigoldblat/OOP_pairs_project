
class Book:
    def __init__(self,titel:str,author:str,ISBN:int):
        self.titel = titel
        self.author = author
        self.ISBN = ISBN
        self.is_available = True
    def __str__(self):
        return f"titel: {self.titel} author: {self.author} is_available: {self.is_available}"