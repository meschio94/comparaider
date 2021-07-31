import logging
from django.http import HttpResponse

# _logger = logging.getLogger(__name__)
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from showcase.models import Maker,Glider


class Homepage(TemplateView):
    template_name = 'index.html'







def get_gliders():
    gliders = Glider.objects.all()

    return gliders

def get_manufactures():
    maker = Maker.objects.all()

    return maker


