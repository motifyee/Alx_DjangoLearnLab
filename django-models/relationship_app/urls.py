from django.urls import path
from flask import views
from .views import all_books, LibraryDetailView, LoginView, LogoutView

urlpatterns = [
    path('books/', all_books, name='books'),
    path('library', LibraryDetailView.as_view(), name='library'),
    path('login', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
]

# views.register
