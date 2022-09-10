from django.contrib import admin

# Register your models here.
from Course_home.models import Level, Course, CourseSessions

admin.site.register(Course)
admin.site.register(Level)

admin.site.register(CourseSessions)