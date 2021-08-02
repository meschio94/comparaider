from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View, TemplateView
from .filters import GliderFilter
from .models import Item, Maker, Glider
# Create your views here.


class IndexView(ListView):
    template_name = 'showcase/index.html'

class Prova(TemplateView):
    template_name = 'showcase/prova.html'
    def get_context_data(self, **kwargs):
        context = super(Prova, self).get_context_data(**kwargs)
        context['gliders'] = Glider.objects.all()
        return context

class Manufactures(TemplateView):
    template_name = 'showcase/manufactures.html'

    def get_context_data(self, **kwargs):
        context = super(Manufactures, self).get_context_data(**kwargs)
        context['manufactures'] = Maker.objects.all()
        return context



class GlidersView(ListView):
    model = Glider
    template_name = 'showcase/index.html'

    def get_context_data(self, **kwargs):
        context = super(GlidersView, self).get_context_data(**kwargs)
        context['gliders'] = GlidersView.objects.all()
        context['glidersprova'] = "prova"
        return context

class User(TemplateView):
    template_name = 'user.html'


def gliders():

    return "prova"

def glider_list(request):
    model = Glider.objects.all()
    myFilter = GliderFilter(request.GET, queryset=model)
    model = myFilter.qs
    context = {
        'myFilter': myFilter,
        'gliderlist':model,
    }
    return render(request,'index.html', context)

def view_glider_table(request, id=None):
    instance = get_object_or_404(Glider, id=id)
    context={
        'instance':instance
    }
    return render(request, 'showcase/modal_glider.html')
