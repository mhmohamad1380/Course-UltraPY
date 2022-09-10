from django.db import models

# Create your models here.
from Course_home.models import Course
from User.models import User


class FavoriteCourses(models.Model):
    favorite_courses = models.ForeignKey(Course,null=True, verbose_name='دوره های مورد علاقه',on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'دوره مورد علاقه'
        verbose_name_plural = 'دوره های مورد علاقه'
