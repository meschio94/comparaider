from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import UserCreationForm, PersonSignUpForm
from members.models import User

# Create your views here.

class PersonCreationView(CreateView):
    form_class = PersonSignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('showcase:home')

class LoginView(TemplateView):
    form_class = PersonSignUpForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('showcase:home')