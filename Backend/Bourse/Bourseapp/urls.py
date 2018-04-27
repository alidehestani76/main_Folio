from django.conf.urls import url , include
from . import views
urlpatterns=[
    url(r'^$',views.Bourse) ,
]


#faghat yadam bemoone:D
urlpatterns = [
    url(r'^search/$', views.Bourse),
]
