from django.contrib import admin

# Register your models here.


from .models import comment_list


class comments_displ(admin.ModelAdmin):
    models = "comment_list"
    list_display = ["cid","uid","fid","comments","comment_post_time"]


admin.site.register(comment_list , comments_displ)
