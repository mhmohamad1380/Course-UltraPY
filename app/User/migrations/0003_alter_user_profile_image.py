# Generated by Django 3.2.6 on 2021-09-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile-image', verbose_name='تصویر کاربری'),
        ),
    ]
