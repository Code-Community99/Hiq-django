from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

handler404 = views.handle404

urlpatterns = [
    url("" , include("home.urls")),
    url('admin/', admin.site.urls),
    url("login/" , include("login.urls")),
    url("signup/" , include("signup.urls")),
    url("events/" , include("events.urls")),
    url("profile/" , include("uprofile.urls")),
    url("upload/" , include("upload_pro.urls")),
    url("developers/" , include("developers.urls")),
    url("logout/" , include("logout.urls")),
    url("gallery/" , include("gallery.urls")),
    url("Feeds/" , include("Feeds.urls")),
    url("comments/" , include("comments.urls")),
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
