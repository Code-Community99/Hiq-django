from django.conf.urls import url

from . import views
app_name = "home"

urlpatterns = [
    url("^$" , views.home , name = "home"),
]


handler404 = views.handle404
