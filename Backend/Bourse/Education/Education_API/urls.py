from django.conf.urls import url , include
from . import views


urlpatterns = [
    url(r'^all_videos/',views.EduListAPIView.as_view()) ,
    #information about a user
    #url(r'^special_video/(?P<username>\w{0,50})/$', views.EduDetailsAPIView.as_view()),
]

