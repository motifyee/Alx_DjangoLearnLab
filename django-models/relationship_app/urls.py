from django.urls import path
from .views import all_books, LibraryDetailView

urlpatterns = [
    path('books/', all_books, name='books'),
    path('library', LibraryDetailView.as_view(), name='library')
    path('logout', LogoutView.as_view(template_name="logout.html"), name='logout')
    path('login', LoginView.as_view(template_name="login.html"), name='login')
]
