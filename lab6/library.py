"""Dependency injection example, libraries module."""

class Library():
    """Example library."""

    def __init__(self, book):
        """Initializer."""
        self.book = book  # Book is injected