from django.db import models

# Create your models here.
class signup_user(models.Model):
    uid = models.AutoField(primary_key = True)
    First_Name = models.CharField(max_length = 30)
    Second_name = models.CharField(max_length = 30)
    Password = models.CharField(max_length = 30)
    Email = models.EmailField(max_length = 30 , unique = True)
    Phone_Number = models.CharField(max_length = 30)
    profilepic = models.ImageField(max_length = 100 , default = "None")
    logstatus = models.BooleanField(max_length = 3 , default = False)

    class Meta:
        db_table = "users"
