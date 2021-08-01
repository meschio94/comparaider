import logging

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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

        #context['gliders'] = model
        context['myFilter'] = myFilter
        context['manufactures'] = get_manufactures()

        page = self.request.GET.get('page', 1)
        paginator = Paginator(model, 2)

        #parte paginatore con numeri manuale
        #page_number = self.request.GET.get('page')
        #page_obj = paginator.get_page(page_number)
        #context['gliders'] = page_obj
        #fine parte paginatore manuale

        try:
            gliders = paginator.page(page)
        except PageNotAnInteger:
            gliders = paginator.page(1)
        except EmptyPage:
            gliders = paginator.page(paginator.num_pages)

        context['gliders'] = gliders
        return context



def get_gliders():
    gliders = Glider.objects.all()

    return gliders

def get_manufactures():
    maker = Maker.objects.all()

    return maker


