# Generated by Django 3.2.6 on 2021-09-03 17:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20210903_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='time_created_token',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 9, 3, 17, 22, 52, 682990, tzinfo=utc), verbose_name='تاریخ ایجاد توکن'),
        ),
    ]
