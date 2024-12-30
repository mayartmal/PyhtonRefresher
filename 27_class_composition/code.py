class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Book shelf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Book {self.name}"


book = Book("HP")
book2 = Book("SH")
shelf = BookShelf(book2, book)


print(shelf)
print(shelf.books)