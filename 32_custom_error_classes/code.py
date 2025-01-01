#class ToManyPagesReadError(Exception):
class ToManyPagesReadError(ValueError):
    pass



class Book:
    def __init__(self, name: str, page_count:int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0


    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages of {self.page_count}"
        )

    def read(self, pages: int):
        if self.pages_read +pages > self.page_count:
            raise ToManyPagesReadError(
                f"Pages count boundary error"
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages of {self.page_count}")

HP = Book("HP", 500)
try:
    HP.read(50)
except ToManyPagesReadError as e:
    print(e)

try:
    HP.read(510)
except ToManyPagesReadError as e:
    print(e)
