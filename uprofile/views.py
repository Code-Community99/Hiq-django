from django.shortcuts import render,redirect
from upload_pro.models import project
from signup.models import signup_user
from events.models import events_list
import datetime

from django.http import HttpResponse
# Create your views here.


def profile_viewer(request):
    uname = ""
    events_list.objects.filter(eventup_date__lte = datetime.datetime.now()).delete()
    try:
        statusdecision = signup_user.objects.get(Email = request.session["email"]).logstatus

    except:

        uname = "You are not yet logged in."
        return redirect("/login/")

    else:
        if not statusdecision:
            uname = "You are not yet logged in."
            print(statusdecision)
            return redirect("/login/")

        else:
            uname = request.session["email"].split("@")[0]
            usern = request.session["username"]

            userinfo = signup_user.objects.get(Email = request.session["email"])

            return render(request , "./uprofile/user.html" , context = {"projects":project.objects.filter(uid = userinfo.uid) ,
            "userinfo":userinfo , "profile": signup_user.objects.get(Email = request.session["email"]).profilepic, "email":uname , "username":usern})


def update(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        mail = request.POST["email"]

        phone = request.POST["pnumber"]

        uobject = signup_user.objects.get(Email = request.session["email"])
        uobject.First_Name = fname
        uobject.Second_name = lname
        uobject.Email = mail
        uobject.Phone_Number = phone

        try:
            img = request.FILES["imq"]
        except Exception as e:
            uobject.profilepic = img
        else:
            uobject.profilepic = img


        try:
            request.POST["password"][0]

        except Exception as e:
            pass

        else:
            uobject.Password = request.POST["password"]

        request.session["email"] = mail
        request.session["username"] = fname
        # uobject.First_Name
        uobject.save()

    return redirect("/profile/")
