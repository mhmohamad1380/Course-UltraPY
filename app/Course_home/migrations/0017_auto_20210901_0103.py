# Generated by Django 3.2.6 on 2021-08-31 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Course_home', '0016_course_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='buyers',
            field=models.ManyToManyField(blank=True, editable=False, related_name='_Course_home_course_buyers_+', to=settings.AUTH_USER_MODEL, verbose_name='خریداران دوره'),
        ),
        migrations.AlterField(
            model_name='course',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='استاد دوره+', to=settings.AUTH_USER_MODEL, verbose_name='استاد دوره'),
        ),
    ]
