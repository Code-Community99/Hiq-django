from django.db import models

from signup.models import signup_user


class suggetionbox(models.Model):
    sid = models.AutoField(primary_key = True)

    sugguser = models.ForeignKey(signup_user , max_length = 50, on_delete = models.CASCADE)

    suggcontent = models.TextField(max_length = 255)



    class Meta:
        db_table = "suggetions"
