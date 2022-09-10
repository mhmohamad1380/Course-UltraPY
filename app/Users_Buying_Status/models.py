from django.db import models

# Create your models here.
from Course_home.models import Course
from User.models import User


class UsersBuysStatus(models.Model):
    user = models.ForeignKey(User, verbose_name='کاربر', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='دوره های خریداری شده', on_delete=models.CASCADE, null=True,
                               blank=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'اطلاعات خرید کاربر'
        verbose_name_plural = 'اطلاعات خرید کاربران'
