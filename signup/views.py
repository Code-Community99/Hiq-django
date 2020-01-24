from django.shortcuts import render,redirect
from .models import signup_user
# Create your views here.

def signup(request):
    error_log = {}
    if request.method == "POST":
        try:
            signup_user.objects.get(Email = request.POST["email"])

        except Exception as e:

            signup_user.objects.create(First_Name = request.POST["fname"] , Second_name  = request.POST['sname'] ,
            Password = request.POST['password'] , profilepic = request.FILES['profile'], Email = request.POST['email'] , Phone_Number = request.POST['pnumber'])
            return render(request , "./login/login.html")

        else:
            error_log = {"email":"Email is in use by another account. Try another one"}
            return render(request , "./signup/signup.html" , context = {"error_log":[errormessage for errormessage in error_log.values()]})

    else:
        return render(request , "./signup/signup.html")
