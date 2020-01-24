from django.shortcuts import render,redirect
from django.http import HttpResponse
from signup.models import signup_user
# Create your views here.


def logout(request):
    try:
        try:
            loguser = signup_user.objects.get(Email = request.session['email'])
            loguser.logstatus = False
            loguser.save()
            print(signup_user.objects.get(Email = request.session['email']).logstatus)

        except Exception as e:
            print("->>>> {}\n\n".format(e))
            # pass

        # Delete the session data
        # request.session.clear()
        request.session.flush()

    except:
        return HttpResponse("You are not logged in")

    else:
        return redirect("/")

    print(signup_user.objects.get(logstatus = False))
