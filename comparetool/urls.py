from django.conf.urls.static import static
from comparaider.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import include, path
from . import views

app_name = 'comparetool'

urlpatterns = [
                  path('compare/', views.comparator, name='compare'),
                  path('remove/', views.remove_size, name='remove_size'),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
