from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import feeds_list
from signup.models import signup_user
from .forms import feedform
from comments.models import comment_list

from django.db.models import Count

def Feeds(request):

    try:
        statusdecision = signup_user.objects.get(Email = request.session["email"]).logstatus

        request.session["email"]

    except:
        lcontrol = False
        uname = "You are not yet logged in."
        return redirect("/login")

    else:
        lcontrol = True
        if request.method == "POST":
            pass

        else:

            updates = feeds_list.objects.order_by("-post_time").annotate(Count("comment_list__uid"))

            commentcount = []
            print(vars(feeds_list.objects.all()))
            # for x in updates:
            #     commentcount.append(feeds_list.objects.filter(fid = x.Fid))

            online_users = []

            filler = signup_user.objects.filter(logstatus=True)

            for user in filler:
                online_users.append(user.First_Name)

            return render(request , "./Feeds/feed.html" , context = {"updates" : updates,"online_users":online_users , "commentcount":commentcount , "loginshow":lcontrol})




def addFeeds(request):
    useremail = ""

    try:
        useremail = request.session["email"]

    except:
        return redirect("/login/")

    else:

        if request.method =="POST":
            feed = request.POST["feed"]
            uid = signup_user.objects.get(Email = useremail).uid
            feeds_list.objects.create(uid_id = uid, feed = feed)

            return redirect("/Feeds/")

        else:

            form = feedform()
            return render(request , "./Feeds/feed.html" , context = {"form":form})
