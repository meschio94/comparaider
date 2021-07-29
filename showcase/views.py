from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, TemplateView

from .models import Item, Maker, Glider
# Create your views here.



class Prova(TemplateView):
    template_name = 'prova.html'

class Manufactures(TemplateView):
    template_name = 'showcase/manufactures.html'

    def get_context_data(self, **kwargs):
        context = super(Manufactures, self).get_context_data(**kwargs)
        return context

class Gliders(TemplateView):
    template_name = 'gliders.html'

class User(TemplateView):
    template_name = 'user.html'