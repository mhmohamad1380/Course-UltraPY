import os

import moviepy.editor
from django.contrib import messages
from django.http import HttpResponseForbidden, FileResponse
from django.shortcuts import render, redirect

# Create your views here.
from Course_home.models import Course, CourseSessions
from Users_Buying_Status.models import UsersBuysStatus
from courses_videos.models import Video


def uploadfile(request, sessionId, courseId):
    if request.method == 'POST':
        course = Course.objects.get(id=courseId)
        session = CourseSessions.objects.get(id=sessionId)
        if request.user != course.creator:
            return HttpResponseForbidden()
        filename = request.POST.get('filename')
        video = request.FILES.get('file')

        is_free = False
        if 'is_free' in request.POST:
            is_free = True
        Id = Video.objects.create(title=filename, session=session, course=course, video=video, is_free=is_free)
        file, ext = os.path.splitext(str(video))
        print(ext)
        if ext != '.zip':
            Id.duration = int(moviepy.editor.VideoFileClip(Id.video.path).duration)

        else:

            Id.duration = 0
        videos = Video.objects.filter(course__id=courseId).count()
        course.file_count = videos
        course.save()
        Id.save()
        messages.success(request, 'ویدیو با موفقیت آپلود شد')
        return redirect(f'/Courses-List/{courseId}/{course.name}')
    return HttpResponseForbidden()


def create_session(request, courseId):
    if request.method == 'POST':
        session_name = request.POST.get('session_name')
        course = Course.objects.get(id=courseId)
        if request.user != course.creator:
            return HttpResponseForbidden()
        CourseSessions.objects.create(session_title=session_name, session_course=course)
        messages.success(request, 'فصل با موفقیت اضافه شد')
        return redirect(f'/Courses-List/{courseId}/{course.name}')
    return HttpResponseForbidden()
