from django.shortcuts import render,redirect
from .forms import sugfrm
from .models import suggetionbox
def suggest(request):
    frm = sugfrm()
    if request.method=="POST":
        errorlog = ""
        try:
            request.session["email"]

        except Exception as e:
            return redirect ("/login/")

        else:
            try:
                uname = request.POST['uname']

            except Exception as e:
                suggetionbox.objects.create(suggcontent = request.POST["suggcontent"])

            else:
                try:
                    suid = signup_user.objects.get(Email = request.session["email"]).uid

                except Exception as e:
                    errorlog = "No user with your identity is n our system"

                else:
                    suggetionbox.objects.create(sugguser = suid , suggcontent = request.POST["suggcontent"])

            return render( request, "suggestion/suggest.html" , context = {"signup":frm , "errorlog":errorlog})

    else:
        return render( request, "suggestion/suggest.html" , context = {"signup":frm})
