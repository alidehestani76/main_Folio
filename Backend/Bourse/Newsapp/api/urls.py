
from django.conf.urls import url , include

from Newsapp.api import views

urlpatterns = [

    url(r'^see_News/',views.NewsListAPIView.as_view(),name='NewsList') ,


]
