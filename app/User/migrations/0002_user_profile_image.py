# Generated by Django 3.2.6 on 2021-08-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='profile-image', verbose_name='تصویر کاربری'),
        ),
    ]
