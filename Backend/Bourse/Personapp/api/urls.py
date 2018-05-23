from django.conf.urls import url , include
from . import views


urlpatterns = [

    url(r'^users/(?P<username>\w{0,50})/update$', views.UserUpdateAPIView.as_view(), name='user-update'),
    #create user
    url(r'^user/create$', views.UserCreateAPIView.as_view(), name='user-create'),
    #all users informations
    url(r'^person_information',views.UserListAPIview.as_view()) ,
    #information about a user
    url(r'^information/(?P<username>\w{0,50})/$', views.UserDetailsAPIview.as_view()),
    #create what person have
    url(r'^update_what_person_have/(?P<username>\w{0,50})/(?P<namad>\w{0,50})/$',views.UpdateMembership.as_view(),name='user will ...') ,
    #what person have :
    url(r'^person_have/(?P<username>\w{0,50})/$',views.WhatPersonHave.as_view(),name='user has') ,
    #create membership
    url(r'^create_membership/create$', views.CreateMembership.as_view(), name='user-create'),


]

