# Generated by Django 3.2.6 on 2021-09-06 03:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Course_home', '0023_alter_course_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 6, 3, 13, 41, 962564, tzinfo=utc), verbose_name='تاریخ ایجاد دوره'),
        ),
    ]
