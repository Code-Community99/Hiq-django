from django.conf.urls import url
from . import views

app_name = "Feeds"

urlpatterns =[
    url("^$" , views.Feeds , name = "Feeds"),
    url("addFeed/" , views.addFeeds , name = "addFeeds"),
]
