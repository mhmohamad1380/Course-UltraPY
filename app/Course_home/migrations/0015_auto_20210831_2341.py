# Generated by Django 3.2.6 on 2021-08-31 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_home', '0014_auto_20210831_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='videos_count',
            field=models.IntegerField(default=0, editable=False, null=True, verbose_name='تعداد ویدیو ها'),
        ),
        migrations.AlterField(
            model_name='course',
            name='total_duration',
            field=models.CharField(blank=True, editable=False, max_length=120, null=True, verbose_name='زمان دوره'),
        ),
    ]
