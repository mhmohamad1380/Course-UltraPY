from django.contrib import admin

# Register your models here.
from course_comments.models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'time', 'course', 'is_agree']
    list_editable = ['is_agree']


admin.site.register(Comments,CommentsAdmin)
