from django.conf.urls import url
from . import views


app_name = "suggestions"

urlpatterns = [
    url("^$" , views.suggest , name = "suggest"),
    url("^delete/(?P<project_id>[\w]*)/" , views.delete_suggestion , name = "delete"),
    url("^suggestions/(?P<sugid>[\d]*)" , views.post_publoc , name = "suggestion")
]
