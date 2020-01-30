from django.db import models

from signup.models import signup_user


class suggetion_box(models.Model):
    sid = models.AutoField(primary_key = True)

    suggestuser = models.ForeignKey(signup_user , default = 1, max_length = 50, on_delete = models.CASCADE)

    suggestion = models.CharField(max_length = 255 , default="")



    class Meta:
        db_table = "suggetions"



class public_suggetion_box(models.Model):
    sid = models.AutoField(primary_key = True)

    suggestuser = models.ForeignKey(signup_user , default = 1, max_length = 50, on_delete = models.CASCADE)

    suggestion = models.CharField(max_length = 255 , default="")



    class Meta:
        db_table = "psuggetions"
