from django.db import models

from signup.models import signup_user
# Create your models here.


class HiQGallery(models.Model):
    id = models.AutoField(primary_key = True)
    uid = models.ForeignKey(signup_user , on_delete = models.CASCADE)
    imagedescription = models.CharField(max_length = 255)
    image = models.FileField(max_length = 255)
