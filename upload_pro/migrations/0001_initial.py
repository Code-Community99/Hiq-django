# Generated by Django 3.0.2 on 2020-01-31 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('Web', 'Website'), ('Android app', 'Android app'), ('Art & poem', 'Art & poem'), ('Not listed', 'Not listed')], max_length=30, null=True)),
                ('project_description', models.TextField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('uploadtime', models.DateTimeField(auto_now_add=True, null=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.signup_user')),
            ],
            options={
                'db_table': 'projects',
            },
        ),
    ]
