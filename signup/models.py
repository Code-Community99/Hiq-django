from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class signup_user(models.Model):
    uid = models.AutoField(primary_key = True)
    First_Name = models.CharField(max_length = 30)
    Second_name = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 255)
    Email = models.EmailField(max_length = 30 , unique = True)
    Phone_Number = models.CharField(max_length = 30)
    profilepic = CloudinaryField("image")
    logstatus = models.BooleanField(max_length = 3 , default = False)
    admin_status = models.BooleanField(max_length = 3, default = 0)

    class Meta:
        db_table = "users"
