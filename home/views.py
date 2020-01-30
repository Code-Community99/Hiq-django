from django.shortcuts import render
from django.http import HttpResponse
from .forms import loginfrm
from events.models import events_list
import datetime
from signup.models import signup_user
from django.contrib.auth.hashers import make_password


# Create your views here.
def home(request):
    try:
        events_list.objects.filter(eventup_date__lte = datetime.datetime.now()).delete()
    except Exception as e:
        pass
    else:
        pass


    form = loginfrm()
    if "username" in request.session:
        lcontrol = True
    else:
        lcontrol = False
    return render (request , "./home/index.html" , context = {"form": form , "loginshow":lcontrol})


def handle404(request ,exception):
    return HttpResponse("Hello world")
