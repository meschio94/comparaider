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
        context['manufactures'] = Maker.objects.all()
        return context

class Gliders(TemplateView):
    template_name = 'gliders.html'

class User(TemplateView):
    template_name = 'user.html'

class GliderListView(ListView):
    model = Glider
    context_object_name = 'glider_list_view'
    paginate_by = 3
    #template_name = 'templates/cards.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gliderlist'] = Glider.objects.all()
        return context

