from django.shortcuts import render,redirect
from .forms import sugfrm
from django.http import HttpResponse
from .models import suggetion_box , public_suggetion_box
from signup.models import signup_user



def suggest(request):
    try:
        suggestion_access = request.session['email']

    except Exception as e:
        return redirect("/login/")

    else:
        frm = sugfrm()
        suggestion_access = signup_user.objects.get(Email = suggestion_access)
        suggestP = public_suggetion_box.objects.all()

        suggestion_data = suggetion_box.objects.all()
        if request.method=="POST":

            errorlog = ""

            try:
                uname = request.POST['uname']

            except Exception as e:
                suggetion_box.objects.create(suggestion = request.POST["suggestion"])
                return redirect("/suggestions/")

            else:
                try:
                    uid = suggestion_access.uid

                except Exception as e:
                    errorlog = "No user with your identity is n our system"
                    return redirect("/suggestions/")
                    # return render( request, "suggestion/suggest.html" , context = {"signup":frm , "errorlog":errorlog , "access":suggestion_access ,"suggestion_data":suggestion_data})

                else:
                    suggetion_box.objects.create(suggestuser_id = uid , suggestion = request.POST["suggestion"])
                    return redirect("/suggestions/")
                    # return render( request, "suggestion/suggest.html" , context = {"signup":frm , "errorlog":errorlog , "access":suggestion_access})

        else:
            return render( request, "suggestion/suggest.html" , context = {"signup":frm , "access":suggestion_access , "suggestion_data":suggestion_data , "suggestP":suggestP})




def post_publoc(request , sugid):
    try:
            psdata = suggetion_box.objects.get(sid = sugid)
            public_suggetion_box.objects.create(suggestuser_id =  psdata.suggestuser_id, suggestion = psdata.suggestion)

    except Exception as e:

        return redirect("/suggestions/")
    else:
        return redirect("/suggestions/")




def delete_suggestion(request , project_id):
    suggetion_box.objects.get(sid = project_id).delete()
    return redirect("/suggestions/")
