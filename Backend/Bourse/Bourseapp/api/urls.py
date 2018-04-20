from django.conf.urls import url , include
from . import views

urlpatterns = [

    url(r'^api',views.PostListAPIview.as_view()) ,
    url(r'^(?P<id>[0-9]{1,3})',views.PostDetailsAPIview.as_view()),
]