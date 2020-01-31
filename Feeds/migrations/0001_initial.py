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
            name='feeds_list',
            fields=[
                ('Fid', models.AutoField(primary_key=True, serialize=False)),
                ('feed', models.CharField(max_length=1255)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='signup.signup_user')),
            ],
            options={
                'db_table': 'feeds',
            },
        ),
    ]
