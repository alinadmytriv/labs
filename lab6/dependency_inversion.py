class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def getName(self):
        return self.name

    def getAuthor(self):
        return self.author


class Library:
    def __init__(self, name, book):
        self.name = name
        self.book = book

    def addBook(self):
        print(f"Book \"{self.book.getName()}\" add to library \"{self.name}\"")


if __name__ == '__main__':
    book = Book("Romeo & Juliet", "William Shakespeare")
    print(f"Book - {book.getName()}")
    library = Library("Stefanyk National Science Library", book)
    library.addBook()
