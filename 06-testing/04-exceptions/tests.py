import pytest
from book import Book

def test_valid_creation():
    book = Book("1984", "978-1779501127")
    assert(book.isbn == "978-1779501127")
    assert(book.title == "1984")

def test_creation_with_invalid_title():
    with pytest.raises(RuntimeError):
        book = Book(" ","978-1779501127")

def test_creation_with_invalid_isbn():
    with pytest.raises(RuntimeError):
        book = Book("1984", "125-125125125")