from django.shortcuts import render

from django.http import HttpResponse



def handle404(request , exception):
    return render(request , "./error404s.html".format(exception))
