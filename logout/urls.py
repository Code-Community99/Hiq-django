from django.conf.urls import url
from . import views

app_name = "logout"

urlpatterns=[
    url("logout/" , views.logout , name = "logout")
]
