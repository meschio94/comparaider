from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, TemplateView
from .filters import GliderFilter
from .models import Item, Maker, Glider
# Create your views here.



class Prova(TemplateView):
    template_name = 'showcase/prova.html'

class Manufactures(TemplateView):
    template_name = 'showcase/manufactures.html'

    def get_context_data(self, **kwargs):
        context = super(Manufactures, self).get_context_data(**kwargs)
        context['manufactures'] = Maker.objects.all()
        return context

class Gliders(ListView):
    model = Glider
    template_name = 'showcase/cards.html'

    def get_context_data(self, **kwargs):
        context = super(Gliders, self).get_context_data(**kwargs)
        context['gliders'] = Gliders.objects.all()
        return context

class User(TemplateView):
    template_name = 'user.html'



def glider_list(request):
    model = Glider.objects.all()
    #myFilter = GliderFilter(request.GET, queryset=model)
    #model = myFilter.qs
    context = {
        #'myFilter': myFilter,
        'gliderlist':model,
    }
    return render(request,'showcase\cards.html', context)
