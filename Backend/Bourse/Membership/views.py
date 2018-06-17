
from django.http import HttpResponse


from Personapp.models import Person
from Bourseapp.models import Bourse
from Membership.models import MemberShip

def Buy_Sell(request):
    if 'change' in request.GET:
        my_change=request.GET['change'].split('$')
        user_name=my_change[0]
        number_of_stock=int(my_change[1])
        new_money_person_have=int(my_change[2])
        stocks_name=my_change[3]

        un = Person.objects.get(username=user_name)
        bn = Bourse.objects.get(namad=stocks_name)


        is_exist = MemberShip.objects.filter(
            bourse=stocks_name,person=user_name).exists()

        if(is_exist==False and number_of_stock!=0):
            MemberShip.objects.create(bourse=bn,person=un,number_of_stocks_person_has=number_of_stock)
            message='ok'

        else:
            obj=MemberShip.objects.get(bourse=bn , person=un)
            if(number_of_stock==0):
                obj.delete()
                message='bye_bye'
            else:
                obj.number_of_stocks_person_has=number_of_stock
                obj.save()
                message="ok!!"



        un.money=new_money_person_have
        un.save()


        return HttpResponse(message)


    return HttpResponse('bad request :D')

