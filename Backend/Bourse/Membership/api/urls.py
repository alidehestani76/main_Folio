from django.conf.urls import url , include
from . import views


urlpatterns = [

    #create what person have
    url(r'^update_what_person_have/(?P<username>\w{0,50})/(?P<namad>\w{0,50})/$',views.UpdateMembership.as_view(),name='user will ...') ,
    #what person have :
    url(r'^person_have/(?P<username>\w{0,50})/$',views.WhatPersonHave.as_view(),name='user has') ,
    #create membership
    url(r'^create_membership/create$', views.CreateMembership.as_view(), name='user-create'),


]

