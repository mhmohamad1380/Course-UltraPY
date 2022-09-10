# Generated by Django 3.2.6 on 2021-09-06 04:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesettings',
            name='feature_3',
            field=models.CharField(max_length=120, null=True, verbose_name='ویژگی ۳'),
        ),
        migrations.AlterField(
            model_name='homesettings',
            name='logo',
            field=models.ImageField(null=True, upload_to='settings', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])], verbose_name='لوگوی سایت'),
        ),
    ]
