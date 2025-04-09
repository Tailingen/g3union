from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from users.forms import LoginUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

#    def get_success_url(self):
#        return reverse_lazy('home')

#class LogoutUser(LogoutView):
#    extra_context = {'title': 'Страница выхода'}

def logout(request):
    return HttpResponse('Страница выхода')
