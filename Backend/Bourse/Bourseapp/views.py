from django.http import HttpResponse
from django.shortcuts import render
from Bourseapp.models import Bourse
from Bourseapp.cron import From_Bourse
from Personapp.models import Person

# def Bourse(request) :
#     b=Bourse()
#     a=From_Bourse()
#     b.name=a.name
#
#     return render(request,'Bourse.html',{'n':n})

#faghat yadam bemoone:D
def Bourse(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     file1 = open("/home/wt/Desktop/hasan.txt", "a")
#     file1.write(request.GET['q'])

    my_q=request.GET['q'].split('*')
    is_exist = Person.objects.filter(user_name=my_q[0]).exists()
    if(is_exist==True):message='repeated username'
    else:
        message='created'
        person=Person()
        person.user_name=my_q[0]
        person.name = my_q[1]
        person.lastname =my_q[2]
        person.save()

    return HttpResponse(message)