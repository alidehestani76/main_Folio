from django.conf.urls import url , include

from login import views

urlpatterns=[
    url(r'^in/',views.lol) ,
    url(r'^out/',views.log_out),
]