from django.conf.urls import url
from . import views

app_name = "profile"


urlpatterns = [
    url("^$" , views.profile_viewer , name = "profile"),
    url("update/" , views.update , name = "update"),

]
