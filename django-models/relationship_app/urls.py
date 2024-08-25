from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.urls import path
from flask import views
from .views import (
  list_books, all_books , LibraryDetailView, LoginView, LogoutView,
  admin_view, librarian_view, member_view
)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/signup.html'


urlpatterns = [
    path('books/', all_books, name='books'),
    path('add_book/add/', add_book, name="add_book"),
    path('edit_book/<int:pk>/edit/', edit_book, name="edit_book"),
    path('delete_book/<int:pk>/delete/', delete_book, name="delete_book"),
    
    path('library', LibraryDetailView.as_view(), name='library'),
    path('login', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register', UserCreationForm(), name="templates/relationship_app/register.html", name='register')

    # Role-based views URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

# views.register
