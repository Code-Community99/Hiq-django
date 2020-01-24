from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import galform

from .models import HiQGallery
from signup.models import signup_user

def photos(request):
    uploadimage = HiQGallery.objects.order_by("id")

    form = galform()
    if request.method =="POST":

        email = ""

        try:
            statusdecision = signup_user.objects.get(Email = request.session["email"]).logstatus

            request.session['email']

        except Exception as e:
            lcontrol = False
            uname = "You are not yet logged in."
            return redirect("/login/")

        else:
            lcontrol = True
            try:

                email = signup_user.objects.get(Email = request.session['email']).uid

            except Exception as e:
                print("{}\n\n\n\n\n\n\n\n\n\n".format(e))
                return redirect("/login/")

            else:
                getuid = email
                HiQGallery.objects.create(image = request.FILES['image'], uid_id = getuid, imagedescription = request.POST['imagedescription'])

                hqgallery = HiQGallery.objects.all()
                return render(request , "./gallery/gallery.html" , context = {"gallery":hqgallery , "uploadimage":uploadimage , "loginshow":lcontrol , "uploadimage":form})

    else:
        hqgallery = HiQGallery.objects.all()
        # uploaduser
        lcontrol = False
        try:
            statusdecision = signup_user.objects.get(Email = request.session["email"]).logstatus

            request.session['email']

        except Exception as e:
            lcontrol = False
            return render(request , "./gallery/gallery.html" , context = {"gallery":hqgallery , "uploadimage":uploadimage , "uploadimage":form , "loginshow":lcontrol })

        else:
            lcontrol = True
            hqgallery = HiQGallery.objects.all()
            return render(request , "./gallery/gallery.html" , context = {"gallery":hqgallery , "uploadimage":uploadimage , "uploadimage":form , "loginshow":lcontrol })




def uploadphotos(request):
    if request.method == "POST":
        try:
            HiQGallery.objects.create(uid_id = signup_user.objects.get(Email = request.session["email"]).uid ,
            image = request.FILES["image"])

            return redirect("/gallery")

        except KeyError as e:
            return redirect("/login/")

        else:
            pass

    else:
        pass

    frm = galform
    return render(request , "./gallery/uploadgal.html" ,  context = {"up":frm})
