from django.contrib import admin

# Register your models here.

from .models import events_list


class event_display(admin.ModelAdmin):
    model = events_list
    list_display = ["event_id","event_organizer","event_description","event_post_date"]
    class Meta:
        pass

admin.site.register(events_list,event_display)
