from django.conf.urls.static import static
from django.contrib import admin
from comparaider.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import include, path

# from members.views import PersonSignUpView
from members.views import PersonCreationView, LoginView
from showcase import urls
from comparaider.views import Homepage
from showcase.views import gliders
import showcase.views
from showcase import urls

app_name = 'members'

urlpatterns = [
                  # path('', include('showcase.urls')),
                  # path('accounts/', include('django.contrib.auth.urls')),
                  path('login/', LoginView.as_view(), name='login'),
                  path('signup/', PersonCreationView.as_view(), name='signup'),
                  # path('accounts/signup/person/', PersonSignUpView.as_view(), name='person_signup'),
                  # path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
