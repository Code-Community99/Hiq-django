from django.contrib import admin
from .models import home_data
# Register your models here.

class home_data_disp(admin.ModelAdmin):
    model = 'home_data'
    fields = ['']

# admin.site.register(home_data , home_data_disp)
