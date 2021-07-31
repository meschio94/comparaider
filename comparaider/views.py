import logging
from django.http import HttpResponse

# _logger = logging.getLogger(__name__)
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from showcase.filters import GliderFilter
from showcase.models import Maker,Glider
from showcase.views import gliders


class Homepage(TemplateView):
    template_name = 'showcase/index.html'


    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)

        model = Glider.objects.all()
        myFilter = GliderFilter(self.request.GET, queryset=model)
        model = myFilter.qs

        context['gliders'] = model
        context['myFilter'] = myFilter
        context['manufactures'] = get_manufactures()

        return context



def get_gliders():
    gliders = Glider.objects.all()

    return gliders

def get_manufactures():
    maker = Maker.objects.all()

    return maker


