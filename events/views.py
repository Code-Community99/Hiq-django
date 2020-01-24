from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import eventfrm
from .models import events_list
import datetime
# Create your views here.
from signup.models import signup_user

def events(request):
    try:
        statusdecision = signup_user.objects.get(Email = request.session["email"]).logstatus
        request.session['email']

    except Exception as e:
        lcontrol = False
        uname = "You are not yet logged in."
        return redirect("/login/")

    else:
        lcontrol = True
        if not statusdecision:
            uname = "You are not yet logged in."
            print(statusdecision)
            return redirect("/login/")

        else:
            events_list.objects.filter(eventup_date__lte = datetime.datetime.now()).delete()
            event_var = events_list.objects.all().order_by("eventup_date")
            # signup_user.objects.get()

            try:
                sess = request.session["username"]

            except:

                sess = ""

            return render(request , "./events/events.html" , context = {"events":event_var, "username":sess , "loginshow":lcontrol})



def add_event(request):
    errorlog = ""
    print("{}\n\n\n\n\n\n\n\n".format(request.POST['description']))
    if request.method=='POST':

        try:
            uname = request.session["email"]

        except:
            errorlog = "Please login to continue"
            uname = "Anornymous"
            return render(request , "./events/addevents.html" , context = {"events":eventfrm,"errorlog":errorlog})

        else:
            events_list.objects.create(event_organizer_id = signup_user.objects.get(Email = request.session["email"]).uid,
            event_venue = request.POST['location'], event_description = request.POST['description'],
            eventup_date = request.POST["eventup_date"])

            return redirect("/events/")

    else:

        return render(request , "./events/addevents.html" , context = {"events":eventfrm})
