from django.contrib import admin
from django.conf.urls import url,include

from . import views

app_name ="gallery"

urlpatterns = [
    url("^$" , views.photos , name = "view_photo"),
    url("galleryup/" , views.uploadphotos , name = "upload_photo"),
]
