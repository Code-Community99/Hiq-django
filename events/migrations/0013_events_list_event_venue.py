# Generated by Django 3.0 on 2020-01-21 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20200121_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='events_list',
            name='event_venue',
            field=models.TextField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
