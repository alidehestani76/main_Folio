from django.conf.urls import url , include
from . import views


urlpatterns = [
    url(r'^posts/(?P<id>\d+)/update$', views.PostUpdateAPIView.as_view(), name='post-update'),
    url(r'^user/create$', views.UserCreateAPIView.as_view(), name='user-create'),
    url(r'^all_information',views.PostListAPIview.as_view()) ,
    url(r'^info/(?P<username>\w{0,50})/$', views.PostDetailsAPIview.as_view()),

]

