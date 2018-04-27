from django.conf.urls import url , include
from . import views


urlpatterns = [

    url(r'^api',views.PostListAPIview.as_view()) ,
    # url(r'^(?P<id>[0-9]{1,3})',views.PostDetailsAPIview.as_view()),
    #url(r'^(?P<namad>)',views.PostDetailsAPIview.as_view()),
    #url(r'^(?P<namad>\w+)$', views.PostDetailsAPIview.as_view()),        #.as_view() to turn Class into Vie

    #url(r'^apii/(?P<namad>\d+)/$',views.PostDetailsAPIview.as_view()),
    url(r'^info/(?P<namad>\w{0,50})/$', views.PostDetailsAPIview.as_view()),

]

