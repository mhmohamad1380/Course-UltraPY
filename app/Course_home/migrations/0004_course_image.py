# Generated by Django 3.2.6 on 2021-08-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_home', '0003_auto_20210829_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='courses_image', verbose_name='تصویر دوره'),
        ),
    ]