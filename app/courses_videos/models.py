import os
import random

import convert_numbers
from django.core import validators
from django.db import models
import moviepy.editor

# Create your models here.
from Course_home.models import Course, CourseSessions


def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return hours, mins, seconds


def get_filename(basename):
    basename1 = os.path.basename(basename)
    name, ext = os.path.splitext(basename1)
    return name, ext


video_name = ''


def video_path(instance, filename):
    new_name = random.randint(1, 1000000)
    name, ext = get_filename(filename)
    new_name1 = f'video_{new_name}.{ext}'
    return f"Course_Videos/{new_name1}"


class Video(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True, verbose_name='عنوان ویدیو')
    course = models.ForeignKey(Course, null=True, blank=False, verbose_name='متعلق به کدام دوره است',
                               on_delete=models.CASCADE)
    session = models.ForeignKey(CourseSessions, null=True, blank=False, on_delete=models.CASCADE,
                                verbose_name='سرفصل دوره')
    video = models.FileField(upload_to=video_path, blank=False, null=True, verbose_name='ویدیو',
                             validators=[validators.FileExtensionValidator(['mkv', 'mp4', 'avi','zip'])])
    is_free = models.BooleanField(default=False, verbose_name='رایگان؟')
    duration = models.PositiveIntegerField(default=0, verbose_name='زمان ویدیو')

    def __str__(self):
        if self.title:
            return self.title
        else:
            return str(self.id)

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیوها'


