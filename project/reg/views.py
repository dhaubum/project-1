from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *

def about(request):
    return render(request, 'reg/about.html')

    
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'reg/register.html'
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('about')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'reg/login.html'

    def get_success_url(self):
        return reverse_lazy('about')


def logout_user(request):
    logout(request)
    return redirect('login')