from django.urls import path

from showcase.views import *

# importarsi le view che useremo mano a mano

app_name = 'showcase'  # evita i confilitti con nomi simili in altre app

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('prova/', Prova.as_view(), name='prova'),
]
