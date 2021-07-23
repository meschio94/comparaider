import logging
from django.http import HttpResponse

#_logger = logging.getLogger(__name__)

def home(request):
    return HttpResponse("Ciao Mondo questa è la home")