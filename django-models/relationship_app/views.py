
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def all_books(request):
    template_name = 'relationship_app/list_books.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        library_name = ""

        context = super().get_context_data(**kwargs)

        library = Library.objects.get(name=library_name)
        context['library'] = library


def LoginView(request):
    # template_name = 'relationship_app/login.html'
    return render(request, 'relationship_app/login.html')


def LogoutView(request):
    # template_name = 'relationship_app/logout.html'
    return render(request, 'relationship_app/logout.html')
