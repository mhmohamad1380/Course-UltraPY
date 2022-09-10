from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from Course_home.models import Course
from User.models import User

admin.site.register(User, UserAdmin)

UserAdmin.fieldsets[2][1]['fields'] = (
    'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_teacher', 'forgot_password_token',
    'time_created_token')
UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', 'profile_image')
UserAdmin.list_display += ('is_teacher', 'is_active')
