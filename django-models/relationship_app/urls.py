from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.urls import path
from flask import views
from .views import all_books, LibraryDetailView, LoginView, LogoutView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/signup.html'


urlpatterns = [
    path('books/', all_books, name='books'),
    path('library', LibraryDetailView.as_view(), name='library'),
    path('login', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register', UserCreationForm(), name="templates/relationship_app/register.html", name='register')
]

# views.register
