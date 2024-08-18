from django.shortcuts import render
from django.http import HttpResponse
from relationship_app.models import Book, Library


def all_books(request):
    books = Book.objects.all()
    return HttpResponse(books)


class LibraryView(ListView):
    model = Library

    def get_context_data(self, **kwargs):
        library_name = ""

        context = super().get_context_data(**kwargs)

        library = Library.objects.get(name=library_name)
        context['library'] = library
