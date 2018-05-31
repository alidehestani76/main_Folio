from . import views.py
from django.conf.urls import url , include

urlpatterns = [

    url(r'^see_News/',views.NewsListAPIView.as_view(),name='NewsList') ,


]
