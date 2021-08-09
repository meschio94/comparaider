from django.conf.urls.static import static
from django.contrib import admin
from . import views
from comparaider.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import include, path

# from members.views import PersonSignUpView
from members.views import PersonCreationView, LoginView
from showcase import urls
from comparaider.views import Homepage
from showcase.views import gliders
import showcase.views
from showcase import urls

app_name = 'reviews'

urlpatterns = [
                  path('add_review/<int:pk>/', views.add_review, name='add_review'),
                  path('add_review/<int:pkg>/<int:pkr>', PersonCreationView.as_view(), name='edit_review'),

               ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
