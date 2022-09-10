# Generated by Django 3.2.6 on 2021-09-08 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Course_home', '0027_alter_course_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_courses', models.ManyToManyField(to='Course_home.Course', verbose_name='دوره های مورد علاقه')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'دوره مورد علاقه',
                'verbose_name_plural': 'دوره های مورد علاقه',
            },
        ),
    ]