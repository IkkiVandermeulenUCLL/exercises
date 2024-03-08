class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_books(self, search_string):
        result =[]
        for x in self.books:
            if search_string.lower() in x.title.lower() or search_string.lower() in x.author.lower():
                result.append(x)
        return result