from django.conf.urls import url , include
from . import views


urlpatterns = [
    #it will show all information
    url(r'^all_information',views.StockListAPIview.as_view()) ,
    #it will show information about one namad:D
    url(r'^info/(?P<namad>\w{0,50})/$', views.StockDetailsAPIview.as_view()),

]

