from django.db import models

# Create your models here.
from signup.models import signup_user

class events_list(models.Model):
    event_id = models.AutoField(primary_key = True)
    event_organizer = models.ForeignKey(signup_user , on_delete = models.CASCADE)
    event_description = models.TextField(max_length = 255)
    event_venue = models.TextField(max_length = 255)
    eventup_date = models.DateTimeField(max_length = 30)
    event_post_date = models.DateTimeField(auto_now_add=True)
    # eventDate = models.DateField(max_length = 40)

    class Meta:
        db_table = "events"

    def __str__(self):
        return self.event_description
