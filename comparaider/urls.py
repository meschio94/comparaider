"""comparaider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from showcase import urls
from comparaider.views import Homepage, get_gliders

import showcase.views
from showcase import urls



urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('showcase/', include('showcase.urls')),
    #path('prova', get_gliders, name='prova'),
    path('admin/', admin.site.urls),

]
