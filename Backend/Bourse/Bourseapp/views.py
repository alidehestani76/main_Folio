from django.shortcuts import render
from Bourseapp.models import Bourse
from Bourseapp.cron import From_Bourse

def Bourse(request) :
    b=Bourse()
    a=From_Bourse()
    b.name=a.name

    return render(request,'Bourse.html',{'n':n})
