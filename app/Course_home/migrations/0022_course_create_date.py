# Generated by Django 3.2.6 on 2021-09-06 03:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Course_home', '0021_rename_zip_count_course_file_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='create_date',
            field=models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='تاریخ ایجاد دوره'),
        ),
    ]
