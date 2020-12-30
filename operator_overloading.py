class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        total_pages=self.pages+other.pages
        return total_pages

book1=Book(100)
book2=Book(200)
book3=Book(500)
print(book1+book2)
print(book2+book3)
print(book1+book3)

