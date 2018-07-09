from django.http import HttpResponse , JsonResponse

from Personapp.models import Person


def lol(request):

    if 'login' in request.GET:
        #return HttpResponse("kirete")
        #message = 'You searched for: %r' % request.GET['q']

        my_q=request.GET['login'].split('*')
        is_exist = Person.objects.filter(name=my_q[0],password=my_q[1]).exists()
        # if session doesnt exist:

        if(is_exist==True):
            #if request.session["username"] == my_q[0] :
            if request.session.has_key("username"):
                if request.session["username"] == my_q[0]:
                    return JsonResponse({'result': True , 'info':"already logged in"})

            request.session["username"] = my_q[0]
            return JsonResponse({'result': True, 'info': "logged in successfully"})
        else:
            return JsonResponse({'result': False, 'info': "Wrong username or password"})

    else :
        return JsonResponse({'result': False, 'info': "already logged in"})



def log_out(request):
    if 'logout' in request.GET:
        my_q = request.GET['logout'].split('*')
        is_exist = Person.objects.filter(name=my_q[0]).exists()

        if request.session.has_key("username"):
            if request.session["username"]==my_q[0]:
                request.session.pop("username")
                return JsonResponse({'result': True, 'info': "logged out successfully"})
            else:
                return JsonResponse({'result': True, 'info': "not found"})
        else:
            return JsonResponse({'result': True, 'info': "not logged in"})
            
    else:
        return JsonResponse({'result': True, 'info': "false form"})
