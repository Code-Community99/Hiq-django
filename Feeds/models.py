from django.db import models

from signup.models import signup_user

# Create your models here.
class feeds_list(models.Model):
    Fid = models.AutoField(primary_key = True)
    uid = models.ForeignKey(signup_user , on_delete = models.CASCADE)
    feed = models.CharField(max_length = 1255)
    post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "feeds"

    def _str__(self):
        return self.feed
