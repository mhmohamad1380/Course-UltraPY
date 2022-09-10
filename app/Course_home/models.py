from django import forms
from django.core import validators
import convert_numbers
from django.core.exceptions import ValidationError
from django.contrib.humanize.templatetags import humanize
from django.utils import timezone
from tinymce.models import HTMLField

from User.models import User
from django.db import models

# Create your models here.
from extensions.utils import jalali_date

levels = (('مبتدی', 'مبتدی'),
          ('متوسط', 'متوسط'),
          ('پیشرفته', 'پیشرفته'))


class Level(models.Model):
    level = models.CharField(max_length=120, blank=False, null=True, verbose_name='سطح')

    class Meta:
        verbose_name = 'سطح'
        verbose_name_plural = 'سطوح'

    def __str__(self):
        return self.level


class Course(models.Model):
    name = models.CharField(max_length=120, null=True, blank=False, verbose_name='نام دوره')
    level = models.ManyToManyField(Level, blank=False, verbose_name='سطح')
    creator = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE, verbose_name='استاد دوره')
    image = models.ImageField(upload_to='courses_image', blank=False, null=True, verbose_name='تصویر دوره')
    buyers_count = models.IntegerField(default=0, blank=False, null=True, verbose_name='تعداد خرید دوره', editable=False)
    course_price = models.IntegerField(blank=False, null=True, verbose_name='قیمت دوره')
    course_discount = models.IntegerField(default=0, blank=True, null=True, verbose_name='تخفیف دوره',
                                          validators=[validators.MinValueValidator(0),
                                                      validators.MaxValueValidator(100)])
    discount_person = models.IntegerField(blank=True, null=True, verbose_name='تخفیف تا چه زمانی')
    about_course = HTMLField(max_length=150, null=True, blank=False, verbose_name='درباره دوره')
    what_you_learn = HTMLField(null=True, blank=False, verbose_name='چه چیزی یاد میگیری')
    final_price = models.IntegerField(blank=True, null=True, verbose_name='قیمت دوره', editable=False)
    total_duration = models.CharField(max_length=120, null=True, blank=True, verbose_name='زمان دوره', editable=False)
    videos_count = models.IntegerField(default=0, blank=False, null=True, verbose_name='تعداد ویدیو ها', editable=False)
    is_done = models.BooleanField(default=False, verbose_name='دوره تمام شده؟')
    file_count = models.PositiveIntegerField(default=0, verbose_name='تعداد فایل منتشر شده ', editable=False)
    create_date = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ایجاد دوره', editable=False)
    tags = models.CharField(max_length=340, null=True, blank=False,
                            verbose_name='تگ های دوره را وارد کنید و با , از هم جدا کنید')

    def clean(self):
        if not self.total_duration:
            self.total_duration = 0
        if self.discount_person == self.buyers_count:
            self.final_price = self.course_price
        if not self.discount_person:
            self.discount_person = self.buyers_count
        if self.course_discount == 0 and self.discount_person or self.course_discount > 0 and not self.discount_person:
            raise ValidationError('"تخفیف تا چه زمانی " و "تخفیف دوره" هردو باید اعمال شوند')
        if self.discount_person:
            if self.discount_person <= self.buyers_count:
                raise ValidationError('مقدار "تخفیف تا چه زمانی" باید از "تعداد خرید دوره" بیشتر باشد ')
        self.final_price = self.course_price - (int(self.course_discount) * self.course_price / 100)

    def __str__(self):
        return self.name

    def get_files_count(self):
        return convert_numbers.english_to_persian(int(self.file_count))

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    def get_absolute_url(self):
        return self.name.replace(' ', '-')

    def get_creator_fullname(self):
        return f'{self.creator.first_name} {self.creator.last_name}'

    def get_course_price_persian(self):
        price = []
        final_price = ''
        for num in convert_numbers.english_to_persian(self.course_price):
            price.append(num)
        if len(price) % 2 != 0:
            for n in range(1, (int(len(price) / 3)) + 1):
                index_num = int(-3 * n) - (n - 1)
                price.insert(index_num, ',')
        else:
            for n in range(1, (int(len(price) / 3))):
                index_num = int(-3 * n) - (n - 1)
                price.insert(index_num, ',')
        for c in price:
            final_price += c
        return final_price

    def get_course_final_price_persian(self):
        price = []
        final_price = ''
        for num in convert_numbers.english_to_persian(self.final_price):
            price.append(num)
        if len(price) % 2 != 0:
            for n in range(1, (int(len(price) / 3)) + 1):
                index_num = int(-3 * n) - (n - 1)
                price.insert(index_num, ',')
        else:
            for n in range(1, (int(len(price) / 3))):
                index_num = int(-3 * n) - (n - 1)
                price.insert(index_num, ',')
        for c in price:
            final_price += c
        return final_price

    def get_jalali_date(self):
        return jalali_date(self.create_date)


class CourseSessions(models.Model):
    session_title = models.CharField(max_length=240, blank=False, null=True, verbose_name='سرتیتر فصل')
    session_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='فصل مرتبط به کدام دوره است؟')

    def __str__(self):
        return self.session_title

    class Meta:
        verbose_name = 'سرفصل دوره'
        verbose_name_plural = 'سرفصل های دوره'
