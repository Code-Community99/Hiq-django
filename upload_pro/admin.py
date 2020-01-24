from django.contrib import admin

# Register your models here.
from .models import project

class project_disp(admin.ModelAdmin):
    model = project
    list_display = ["uid","project_name","project_description" ,"file","uploadtime"]

admin.site.register(project,project_disp)
