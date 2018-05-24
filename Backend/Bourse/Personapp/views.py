from billiard.five import string
from django.db.models import IntegerField, TextField, CharField
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Personapp.models import Person,MemberShip
from Bourseapp.models import Bourse
from pyasn1.type.univ import Integer

#
# def PersonSignUp(request):
#
#     if 'q' in request.GET:
#         my_q=request.GET['q'].split()
#         #nothing in 2 nextlines
#         # file1 = open("/home/wt/Desktop/hasanzz.txt", "a")
#         # file1.write(my_q[0]+my_q[1]+my_q[2])
#
#         is_exist = Person.objects.filter(username=my_q[0]).exists()
#         if(is_exist==True):message='repeated username'
#         else:
#             message='created'
#             person=Person()
#             person.user_name=my_q[0]
#             person.name = my_q[1]
#             person.lastname =my_q[2]
#             person.save()
#
#         return HttpResponse(message)
#     # else :
#     #     return HttpResponse("false form")
#     elif 'login' in request.GET:
#         my_l=request.GET['l'].split('*')
#         input_password=my_l[1]
#         is_exist = Person.objects.filter(user_name=my_l[0]).exists()
#         if(is_exist==True):
#             person=Person.objects.get(username=my_l[0])
#             if(person.password==input_password):
#                 person.log_in=True
#                 # obj = Bourse.objects.get(namad=stock.namad)
#         return HttpResponse('changed')
#
#     elif 'logout' in request.GET:
#         my_l = request.GET['l'].split('*')
#         input_password = my_l[1]
#         is_exist = Person.objects.filter(user_name=my_l[0]).exists()
#         if (is_exist == True):
#             person = Person.objects.get(username=my_l[0])
#             if (person.password == input_password):
#                 person.log_in = False
#         return HttpResponse('changed')
#
#     else:
#         message='shit!!!do it again!!!'
#
def Buy_Sell(request):
    if 'buy' in request.GET:
        my_buy=request.GET['buy'].split('$')
        user_name=my_buy[0]
        num=int(my_buy[1])
        stocks_name=my_buy[2]
        un = Person.objects.get(username=user_name)
        bn = Bourse.objects.get(namad=stocks_name)


        #just for remember it's true at all
        # usermoney=un.getMoney()
        # usermoney+=111
        # un.setMoney(usermoney)
        # un.save()
        #
        #
        #
        # stockvalue=bn.getValue()
        # stockvalue=string(stockvalue)
        # a=0
        # for i in stockvalue:
        #     a*=10
        #     a+=int(i)
        # a+=1000
        # un.setMoney(a+un.getMoney())
        # un.save()

        #convert stock value from textfiled to integer
        stockvalue=bn.getValue()
        stockvalue=string(stockvalue)
        # temp=0
        # for i in stockvalue:
        #     temp*=10
        #     temp+=int(i)
        # temp*=num
        temp=int(stockvalue)
        userMoney=un.getMoney()

        if(userMoney<temp):
            return HttpResponse("not enough money")
        else:
            un.setMoney(userMoney-temp)
            un.save()
        un.save()

        is_exist = MemberShip.objects.filter(
            bourse=stocks_name,person=user_name).exists()

        if(is_exist==False):
            MemberShip.objects.create(bourse=bn,person=un,number_of_stocks_person_has=num)
            message='ok'

        else:
            obj=MemberShip.objects.get(bourse=bn , person=un)
            obj.number_of_stocks_person_has+=num
            obj.save()
            message="ok!!"
        return HttpResponse(message)

    elif 'sell' in request.GET:
        my_buy = request.GET['sell'].split('$')
        user_name = my_buy[0]
        num = int(my_buy[1])
        stocks_name = my_buy[2]
        un = Person.objects.get(username=user_name)
        bn = Bourse.objects.get(namad=stocks_name)

        stockvalue = bn.getValue()
        stockvalue = string(stockvalue)
        temp = 0
        for i in stockvalue:
            temp *= 10
            temp += int(i)
        temp *= num
        userMoney = un.getMoney()

        is_exist = MemberShip.objects.filter(
            bourse=stocks_name, person=user_name).exists()
        if (is_exist == False):
            message = 'see what you have first'

        else:
            un.setMoney(userMoney+temp)
            un.save()
            obj = MemberShip.objects.get(bourse=bn, person=un)
            if (obj.number_of_stocks_person_has < num):
                message = 'see what you have first'
            else:
                obj.number_of_stocks_person_has -= num
                if(obj.number_of_stocks_person_has==0):
                    obj.delete()
                    return HttpResponse('bye_bye')
                message = "ok!!"
            obj.save()
        return HttpResponse(message)


    return HttpResponse('bad request :D')

#