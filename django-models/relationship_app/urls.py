from django.urls import path
from .views import all_books, LibraryDetailView

urlpatterns = [
    path('books/', all_books, name='books'),
    path('library', LibraryDetailView.as_view(), name='library')
]
