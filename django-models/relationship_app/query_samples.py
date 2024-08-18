from relationship_app.models import Book, Librarian, Library

author_books = Book.objects.get(author="author name")
library_books = Library.objects.get(name=library_name, kwargs="books.all()")
library_librarian = Book.objects.get(library="lib")
