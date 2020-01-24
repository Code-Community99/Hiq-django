from django.contrib import admin

# Register your models here.
from .models import HiQGallery

class md(admin.ModelAdmin):
    list_display = ("uid" , "image")


admin.site.register(HiQGallery , md)
