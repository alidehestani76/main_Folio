from django.conf.urls import url , include
from . import views

#faghat yadam bemoone:D
urlpatterns = [
    url(r'^search/$', views.PersonSignUp),
    url(r'^buy_sell/$',views.Buy_Sell),
]
