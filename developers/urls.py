from django.conf.urls import url

from . import views

app_name = "developers"


urlpatterns = [
    url("^$" , views.contact , name = "contact")
]
