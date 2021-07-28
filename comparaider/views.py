import logging
from django.http import HttpResponse

#_logger = logging.getLogger(__name__)
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name= 'index.html'

