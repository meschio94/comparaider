from django.conf.urls.static import static
from . import views
from comparaider.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import include, path

app_name = 'reviews'

urlpatterns = [
                  path('add_review/<int:pk>/', views.add_review, name='add_review'),
                  path('edit_review/<int:pkg>/<int:pkr>', views.edit_review, name='edit_review'),

               ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
