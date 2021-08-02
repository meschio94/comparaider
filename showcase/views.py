from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
        model = Maker.objects.all()

        page = self.request.GET.get('page', 1)
        paginator = Paginator(model, 2)

        try:
            manufactures = paginator.page(page)
        except PageNotAnInteger:
            manufactures = paginator.page(1)
        except EmptyPage:
            manufactures = paginator.page(paginator.num_pages)

        context['manufactures'] = manufactures

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
