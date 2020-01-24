from django.conf.urls import url
from . import views

app_name = "profile"


urlpatterns = [
    url("^$" , views.profile_viewer , name = "profile"),
    url("update/" , views.update , name = "update"),
    url("serchpro/" , views.serchpro , name = "serchpro"),
    url("view_collequeprof/(?P<collequename>[\w]*\D*\w*)" , views.view_collequeprof , name = "view_collequeprof")

]
