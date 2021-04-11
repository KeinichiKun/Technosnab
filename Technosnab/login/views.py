from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import AuthUserForm, RegisterUserForm
from django.urls import reverse_lazy

from django.contrib.auth.models import User

# Create your views here.
class LogView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('orders')

    def get_success_url(self):
        return self.success_url


class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('orders')
    success_msg = 'Пользователь успешно создан'


class LogoutView(LogoutView):
    next_page = reverse_lazy('login')