# Generated by Django 3.2.6 on 2021-08-31 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_home', '0015_auto_20210831_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='دوره تمام شده؟'),
        ),
    ]