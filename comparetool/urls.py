from django.conf.urls.static import static
from django.contrib import admin
from comparaider.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import include, path
from .views import comparator
from . import views

# from members.views import PersonSignUpView
from members.views import PersonCreationView, LoginView
from showcase import urls
from comparaider.views import Homepage
from showcase.views import gliders
import showcase.views
from showcase import urls

app_name = 'comparetool'

urlpatterns = [
                  path('compare/', views.comparator, name='compare'),
                  path('remove/', views.remove_size, name='remove_size'),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
