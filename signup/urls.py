from django.conf.urls import url
from . import views

app_name = "signup"

urlpatterns = [
    url("^$" , views.signup , name = "signup")
]
