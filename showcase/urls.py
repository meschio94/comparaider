from django.urls import path
from . import views
from showcase.views import *
from comparaider.views import Homepage
# importarsi le view che useremo mano a mano

app_name = 'showcase'  # evita i confilitti con nomi simili in altre app

urlpatterns = [
    path('home/', Homepage.as_view(), name='home'),
    path('prova/', Prova.as_view(), name='prova'),
    path('manufactures/', Manufactures.as_view(), name='manufactures'),
    path('gliders/', GlidersView.as_view(), name='gliders'),
    path('user/', User.as_view(), name='user'),
    path('<int:pk>/manufacture_profile/', ShowManufacturesProfileView.as_view(), name='manufacture_profile'),
    path('manufacturer_panel/', views.manufacturer_admin ,name='manufacture_panel'),
    path('add_glider/', views.add_glider, name='add_glider'),
    path('add_size/<int:pk>/', views.add_size, name='add_size'),
    path('edit_glider/<int:pk>/', views.edit_glider, name='edit_glider'),
    path('edit_size/<int:pkg>/<int:pks>/', views.edit_size, name='edit_size'),
    path('remove_size/', views.remove_size, name='remove_size'),
    path('edit_info/', views.edit_info, name='edit_info')
]
