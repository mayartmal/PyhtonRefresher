#factory example
class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weight {self.weight} g"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

book = Book("Harry Potter", "hardcover", 1500)
book2 = Book.hardcover("Harry Potter",  1500)
book3 = Book.paperback("Python 101",  1200)

print(Book.TYPES)
print(book.name)
print(book)
print(book2)
print(book3)