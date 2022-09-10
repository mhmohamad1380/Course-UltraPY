from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class HomeSettings(models.Model):
    logo = models.ImageField(upload_to='settings', blank=False, null=True, verbose_name='لوگوی سایت',
                             validators=[validators.FileExtensionValidator(['jpg', 'png'])])
    name = models.CharField(max_length=20, blank=False, null=True, verbose_name='نام سایت')
    title = models.CharField(max_length=60, blank=False, null=True, verbose_name='تبتر سایت')
    caption = models.CharField(max_length=120, blank=False, null=True, verbose_name='متن زیر تیتر سایت')
    background_picture = models.ImageField(upload_to='settings', blank=False, null=True,
                                           verbose_name='تصویر پس زمینه سایت')
    feature_1 = models.CharField(max_length=120, null=True, blank=False, verbose_name='ویژگی ۱')
    feature_2 = models.CharField(max_length=120, null=True, blank=False, verbose_name='ویژگی ۲')
    feature_3 = models.CharField(max_length=120, null=True, blank=False, verbose_name='ویژگی ۳')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تنظیم سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def clean(self):
        if self.background_picture.width < self.background_picture.height:
            raise ValidationError('تصویر باید ۱۶:۹ باشد')
