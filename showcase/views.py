from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View


from .models import Item, Maker, Glider
# Create your views here.



class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home.html"