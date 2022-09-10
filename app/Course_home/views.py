import os

from django.contrib import messages
from django.core.mail import send_mail
from importlib._common import _

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse, FileResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
import convert_numbers
# Create your views here.
from django.utils.encoding import force_text
from django.views.generic import ListView
import moviepy.editor

from Course_home.models import Course, CourseSessions
from Users_Buying_Status.models import UsersBuysStatus
from course_account.models import FavoriteCourses
from course_comments.forms import CommentForm
from course_comments.models import Comments
from course_settings.models import HomeSettings
from courses_videos.models import Video
from django.http import HttpResponseNotAllowed


def homepage(request):
    messages.info(request,'توجه : این یک نمونه تستی از سایت اصلی است')
    courses = Course.objects.all()
    settings = HomeSettings.objects.first()
    context = {
        'courses': courses,
        'settings': settings, }
    return render(request, 'home.html', context)


def header(request):
    settings = HomeSettings.objects.first()
    return render(request, 'base/Header.html', {'settings': settings})


def header_other(request):
    setting: HomeSettings = HomeSettings.objects.first()
    return render(request, 'base/Header_other.html', {'setting': setting})


def drawer(request):
    setting: HomeSettings = HomeSettings.objects.first()
    return render(request, 'base/drawer.html', {'setting': setting})


class CourseView(ListView):
    template_name = 'courses.html'
    paginate_by = 20

    def get_queryset(self):
        return Course.objects.all()


def course_detail(request, Id, Cname):
    if not request.user.is_authenticated:
        messages.warning(request, 'ابتدا باید ثبت نام کنید یا وارد شوید.')
        return redirect('/Login')

    def convert(seconds):
        hours = seconds // 3600
        seconds %= 3600
        mins = seconds // 60
        return hours, mins

    all_duration = 0
    all_duration_str = ''
    course = Course.objects.get(id=Id)
    # course level start

    course_level = ''
    course_level_list = []

    for level in course.level.all():
        course_level_list.append(level.level)
    if len(course_level_list) > 1:
        course_level = f'{course_level_list[0]} تا {course_level_list[-1]}'
    else:
        course_level = course_level_list[0]

    # course level end

    # course sessions start
    sessions = CourseSessions.objects.filter(session_course__id=Id).order_by('id').all()

    # course sessions end
    # course student start
    students_count = convert_numbers.english_to_persian(UsersBuysStatus.objects.filter(course__id=Id).count())
    # course student end
    # course Videos start
    videos: Video = Video.objects.filter(course__id=Id)

    for path in videos:
        all_duration += path.duration
    hours, mins = convert(all_duration)

    if hours != 0:
        all_duration_str = f'{convert_numbers.english_to_persian(hours)} ساعت و {convert_numbers.english_to_persian(mins)} دقیقه '
    elif mins != 0:
        all_duration_str = f'{convert_numbers.english_to_persian(mins)} دقیقه '

    course.total_duration = all_duration_str
    course.videos_count = videos.all().count()
    course.save()
    # course Videos end

    # comments start
    comments = CommentForm(request.POST or None)
    if request.method == 'POST':
        if comments.is_valid():
            comment = comments.cleaned_data['comment']
            c = Comments.objects.create(user=request.user, course_id=Id, comment=comment, is_agree=False)
            send_mail('کامنت',
                      f'یه کامنت برای بررسی داری \n  لینک : {request.META.get("HTTP_HOST")}/my_ultra_admin/course_comments/comments/{c.id}/change/',
                      'ultrapy.education@gmail.com', ['ultrapy.education@gmail.com'])
            messages.success(request, 'کامنت شما با موفقیت ثبت شد . بعد از بازبینی منتشر می شود.')
            return redirect(f'/Courses-List/{Id}/success')

    comments = CommentForm(request.POST or None)

    cmnts = Comments.objects.filter(course__id=Id, is_agree=True).all()
    # comments end

    context = {
        'course': course,
        'course_level': course_level,
        'sessions': sessions,
        'students_count': students_count,
        'videos': videos,
        'all_duration_str': all_duration_str,
        'is_bought': None,
        'is_fav': None,
        'comments': comments,
        'cmnts': cmnts

    }
    fav = FavoriteCourses.objects.filter(user=request.user, favorite_courses=course)
    if fav.exists():
        context['is_fav'] = True
    else:
        context['is_fav'] = False
    user = UsersBuysStatus.objects.filter(user=request.user, course=course).first()
    if user:
        context['is_bought'] = True
    else:
        context['is_bought'] = False
    return render(request, 'course_detail.html', context)


@login_required(login_url='/Login')
def videos_view(request, title):
    return HttpResponseForbidden()


@login_required(login_url='/Login')
def download_video(request, videoId, courseId):
    found_course = Course.objects.get(id=courseId)
    user = UsersBuysStatus.objects.filter(user=request.user, course=found_course).first()
    video = Video.objects.filter(id=videoId).first()
    if not request.user.is_superuser:
        if not video.is_free:
            if user:
                found_video = Video.objects.get(id=videoId)
                title = str(found_video.video.url).split('/')[-1]
                video = get_object_or_404(Video, video='Course_Videos/' + title)
                path, filename = os.path.split(title)
                response = FileResponse(video.video)
                return response
            message = force_text('شما اجازه دانلود این فایل را ندارید. لطفا دوره را خریداری کنید')
            return HttpResponseForbidden(message)
        else:
            found_video = Video.objects.get(id=videoId)
            title = str(found_video.video.url).split('/')[-1]
            video = get_object_or_404(Video, video='Course_Videos/' + title)
            path, filename = os.path.split(title)
            response = FileResponse(video.video)
            return response
    else:
        found_video = Video.objects.get(id=videoId)
        title = str(found_video.video.url).split('/')[-1]
        video = get_object_or_404(Video, video='Course_Videos/' + title)
        path, filename = os.path.split(title)
        response = FileResponse(video.video)
        return response


def delete_session(request, sId):
    session = CourseSessions.objects.filter(id=sId)

    if not session.exists():
        raise Http404()
    if request.user != session.first().session_course.creator:
        return HttpResponseForbidden()
    for video in Video.objects.filter(session__id=sId):
        print(video.video.path)
        os.remove(video.video.path)
    course = Course.objects.get(id=session.first().session_course.id)
    session.first().delete()
    messages.success(request, 'فصل با موفقیت حذف شد')
    videos = Video.objects.filter(course__id=course.id).count()
    course.file_count = videos
    course.save()

    return redirect(request.GET.get('next'))


@login_required(login_url='/Login')
def buy_free_course(request, cId):
    course = Course.objects.filter(id=cId)
    if course.exists():
        if course.first().final_price == 0:
            if UsersBuysStatus.objects.filter(user=request.user, course_id=cId).exists():
                raise Http404()
            UsersBuysStatus.objects.create(user=request.user, course=course.first())
            messages.success(request, 'دوره رایگان با موفقیت به دوره های من اضافه شد.')
            return redirect(request.GET.get('next'))
        raise Http404()
    raise Http404()
