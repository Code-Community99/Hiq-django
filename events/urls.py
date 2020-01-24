from django.conf.urls import url

from . import views

app_name = "events"


urlpatterns = [
    url("^$" , views.events , name = "events"),
    url("add_event/" , views.add_event , name = "add_event"),
]
