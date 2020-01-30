from django.conf.urls import url
from . import views


app_name = "suggestions"

urlpatterns = [
    url("" , views.suggest , name = "suggest"),
]
