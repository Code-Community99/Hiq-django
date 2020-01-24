from django.db import models

# Create your models here.
from signup.models import signup_user
from Feeds.models import feeds_list

class comment_list(models.Model):
    cid = models.AutoField(primary_key = True)
    uid = models.ForeignKey(signup_user,on_delete = models.CASCADE)
    fid = models.ForeignKey(feeds_list , on_delete = models.CASCADE)
    comments = models.TextField(max_length=255)
    comment_post_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "comments"

    def __str__(self):
        return self.comments
