"""Bourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
    hello
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^Bourseapp/', include('Bourseapp.urls')),
    #url(r'^Personapp/', include('Personapp.urls')),
    url(r'^Membership/', include('Membership.urls')),
    url(r'^Bourseapp_api/',include('Bourseapp.api.urls')) ,
    url(r'^Personapp_api/', include('Personapp.api.urls')),
    url(r'^Membership_api/', include('Membership.api.urls')),
    #url(r'^Education/', include('Newsapp.urls')) ,
    url(r'^Newsapp_api/', include ('Newsapp.api.urls')) ,
    url(r'^Education_api/', include('Education.Education_API.urls')),
    url(r'^login/', include('login.urls')),


]
