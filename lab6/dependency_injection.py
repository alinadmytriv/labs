"""Dependency injection example, Library & Books IoC containers."""
from dependency_injector import providers, containers
import library
import book

class Book(containers.DeclarativeContainer):
    """IoC container of book providers."""
    comics = providers.Factory(book.Comics)
    novel = providers.Factory(book.Novels)

class Library(containers.DeclarativeContainer):
    """IoC container of library providers."""
    comics = providers.Factory(library.Library, book=Book.comics)
    novel = providers.Factory(library.Library, book=Book.novel)

if __name__ == '__main__':
    comics_book = Library.comics()
    novel_book = Library.novel()