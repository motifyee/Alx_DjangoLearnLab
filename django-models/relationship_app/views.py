from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, Book


def all_books(request):
    template_name = 'relationship_app/list_books.html'
    books = Book.objects.all()
    return HttpResponse(books)


class LibraryView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        library_name = ""

        context = super().get_context_data(**kwargs)

        library = Library.objects.get(name=library_name)
        context['library'] = library
