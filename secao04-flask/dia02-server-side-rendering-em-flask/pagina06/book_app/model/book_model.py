class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return str(
            {
                "title": self.title,
                "author": self.author,
                "year": self.year,
            }
        )

    pass


book = Book("Suzane: Assassina e Manipuladora", "Ullisses Campbell", "2020")
print(book)
