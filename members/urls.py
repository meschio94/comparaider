from django.conf.urls.static import static
from comparaider.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import include, path

from members.views import PersonCreationView, LoginView

app_name = 'members'

urlpatterns = [
                  path('login/', LoginView.as_view(), name='login'),
                  path('signup/', PersonCreationView.as_view(), name='signup'),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
