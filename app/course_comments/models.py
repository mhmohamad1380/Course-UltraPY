from django.db import models

# Create your models here.
from django.utils import timezone

from Course_home.models import Course
from User.models import User
from extensions.utils import jalali_date


class Comments(models.Model):
    user = models.ForeignKey(User, null=True, verbose_name='کامنت کدام کاربر', on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد')
    course = models.ForeignKey(Course, null=True, verbose_name='کامنت کدام دوره ', on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=False, verbose_name='کامنت')
    is_agree = models.BooleanField(default=False, verbose_name='تایید میشود/نمیشود')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'کامنت دوره'
        verbose_name_plural = 'کامنت های دوره'

    def get_created_time(self):
        return jalali_date(self.time)
