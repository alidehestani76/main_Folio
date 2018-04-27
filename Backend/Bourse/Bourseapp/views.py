from django.http import HttpResponse
from django.shortcuts import render
from Bourseapp.models import Bourse
from Bourseapp.cron import From_Bourse

# def Bourse(request) :
#     b=Bourse()
#     a=From_Bourse()
#     b.name=a.name
#
#     return render(request,'Bourse.html',{'n':n})

#faghat yadam bemoone:D
def Bourse(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    file1 = open("/home/wt/Desktop/hasan.txt", "a")
    file1.write(request.GET['q'])
    return HttpResponse(message)