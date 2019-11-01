"""Dependency injection example, libraries module."""

class Library():
    """Example library."""

    database = []
    def __init__(self, book):
        """Initializer."""
        self.book = book  # Book is injected
        self.database.append(book)
