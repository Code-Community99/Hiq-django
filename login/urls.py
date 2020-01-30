from django.conf.urls import url

from . import views
app_name = "login"

urlpatterns = [
    url("^$" , views.login , name = "login"),
    url("^<slug:param>/" , views.login , name = "login"),
    url("(?P<param>[\w]*)/" , views.login , name = "login"),
]
