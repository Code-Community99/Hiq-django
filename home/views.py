from django.shortcuts import render
from django.http import HttpResponse
from .forms import loginfrm
from events.models import events_list
import datetime

# Create your views here.
def home(request):
    events_list.objects.filter(eventup_date__lte = datetime.datetime.now()).delete()
    form = loginfrm()
    if "username" in request.session:
        lcontrol = True
    else:
        lcontrol = False
    return render (request , "./home/index.html" , context = {"form": form , "loginshow":lcontrol})


def handle404(request ,exception):
    return HttpResponse("Hello world")
