from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils import timezone



class User(AbstractUser):
    is_teacher = models.BooleanField(default=False, verbose_name='اجازه انتشار دوره')
    profile_image = models.ImageField(upload_to='profile-image', blank=True, null=True, verbose_name='تصویر کاربری')
    forgot_password_token = models.CharField(max_length=35, blank=True, verbose_name='توکن فراموشی رمز عبور')
    time_created_token = models.DateField(verbose_name='تاریخ ایجاد توکن', blank=True,
                                          default=timezone.now)



