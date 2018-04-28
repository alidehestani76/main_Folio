from django.conf.urls import url , include
from . import views


urlpatterns = [

    url(r'^all_information',views.PostListAPIview.as_view()) ,
    url(r'^info/(?P<username>\w{0,50})/$', views.PostDetailsAPIview.as_view()),

]

