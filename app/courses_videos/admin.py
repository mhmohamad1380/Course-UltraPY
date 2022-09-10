from django.contrib import admin

# Register your models here.
from courses_videos.models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ['__str__',
                    'course',
                    'session', ]


admin.site.register(Video, VideoAdmin)
