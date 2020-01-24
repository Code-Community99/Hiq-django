from django.conf.urls import url
from . import views

app_name = "upload"

urlpatterns = [
    url("delete_project/(?P<deletedp>[\w]+\D+\w*)/" , views.delete_project , name = "delete_project"),
    url("delete_project/<slug:deletedp>/" , views.delete_project , name = "delete_project"),
    url("^$" , views.upload , name = "upload"),
    url("projects/<str:delpro>/" , views.projects , name = "projects"),

]
