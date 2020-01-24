from django.conf.urls import url
from . import views

app_name = "coms"


urlpatterns =[
    url(r"(?P<feedid>[\d]+)" , views.commentview , name = "comments"),
    url(r"addcomment/" , views.addcomment , name = "addcomment"),
]
