# Generated by Django 3.2.6 on 2021-09-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='forgot_password_token',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='توکن فراموشی رمز عبور'),
        ),
    ]
