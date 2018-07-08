from django.http import HttpResponse

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
                    return HttpResponse("already logged in!")
            message='yes'

            request.session["username"] = my_q[0]
        else:
            message="wrong username or password"


        return HttpResponse(message)

    else :
        return HttpResponse("false form")



def log_out(request):
    if 'logout' in request.GET:
        my_q = request.GET['logout'].split('*')
        is_exist = Person.objects.filter(name=my_q[0]).exists()


        if request.session["username"]==my_q[0]:
            request.session.pop("username")
            return HttpResponse("success")

        else:
            return HttpResponse("not found")

    else:
        return HttpResponse("false form")