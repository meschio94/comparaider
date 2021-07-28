from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, TemplateView

from .models import Item, Maker, Glider
# Create your views here.

class Homepage(TemplateView):
    template_name = 'index.html'

class Prova(TemplateView):
    template_name = 'prova.html'