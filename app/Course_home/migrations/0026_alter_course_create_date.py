# Generated by Django 3.2.6 on 2021-09-06 03:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_home', '0025_alter_course_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 9, 6), verbose_name='تاریخ ایجاد دوره'),
        ),
    ]