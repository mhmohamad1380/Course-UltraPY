# Generated by Django 3.2.6 on 2021-09-06 04:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='settings', validators=[django.core.validators.FileExtensionValidator(['svg'])], verbose_name='لوگوی سایت')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='نام سایت')),
                ('background_picture', models.ImageField(null=True, upload_to='settings', verbose_name='تصویر پس زمینه سایت')),
                ('feature_1', models.CharField(max_length=120, null=True, verbose_name='ویژگی ۱')),
                ('feature_2', models.CharField(max_length=120, null=True, verbose_name='ویژگی ۲')),
                ('feature_3', models.CharField(max_length=120, null=True, verbose_name='ویژگی ۲')),
            ],
            options={
                'verbose_name': 'تنظیم سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]
