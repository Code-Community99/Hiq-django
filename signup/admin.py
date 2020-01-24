from django.contrib import admin
from .models import signup_user

class hiq_users_disp(admin.ModelAdmin):
    model = "hiq_users_disp"
    list_display = ["uid","First_Name" , "Second_name" , "Password" , "Email" , "Phone_Number"]
    class Meta:
        pass



admin.site.register(signup_user , hiq_users_disp)
