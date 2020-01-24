from django.contrib import admin

from .models import feeds_list


class feed_displ(admin.ModelAdmin):
    model = "feeds_list"
    list_display = ["Fid","uid", "feed" , "post_time"]

admin.site.register(feeds_list , feed_displ)
