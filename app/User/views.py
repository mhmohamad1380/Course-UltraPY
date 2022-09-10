import random
import string
import time
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.utils import timezone
from django.views.generic import ListView

import Users_Buying_Status
from Course_home.models import Course
from User.forms import ChangePassword
from User.models import User
from Users_Buying_Status.models import UsersBuysStatus
from courses_videos.models import Video


def forget_password_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if 'email-or-user' in request.POST:
        email_or_user = request.POST.get('email-or-user')
        user_email: User = User.objects.filter(email=email_or_user)
        user_username = User.objects.filter(username=email_or_user)
        if user_username.exists() and not user_username.first().email:
            raise Http404()
        elif user_email.exists() or user_username.exists():
            token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=35))
            try:
                send_mail('بازگردانی اکانت در UltraPY',
                          f'برای تغییر کلمه عبور خود می توانید روی لینک زیر بزنید.اگر شما درخواست نکردید،پیام را نادیده '
                          f'بگیرید.\n لینک بازیابی : {request.META.get("HTTP_HOST")}/forget-password/tokenId={token} \n '
                          f'مدت اعتبار این لینک ۲۴ ساعت می باشد.',
                          'ultrapy.education@gmail.com', [user_email.first().email])
                user: user_email = user_email.first()
                user.forgot_password_token = token
                user.time_created_token = timezone.now()
                user.save()
                messages.info(request,
                              f'ایمیلی حاوی لینک تغییر کلمه عبور برای {email_or_user} ارسال شد.')
                return redirect('/')
            except:
                send_mail('بازگردانی اکانت در UltraPY',
                          f'برای تغییر کلمه عبور خود می توانید روی لینک زیر بزنید.اگر شما درخواست نکردید،پیام را نادیده '
                          f'بگیرید.\n لینک بازیابی : {request.META.get("HTTP_HOST")}/forget-password/tokenId={token} \n '
                          f'مدت اعتبار این لینک ۲۴ ساعت می باشد.',
                          'ultrapy.education@gmail.com', [user_username.first().email])

                user: user_email = user_username.first()
                user.forgot_password_token = token
                user.time_created_token = timezone.now()
                user.save()
                messages.info(request, f'ایمیلی حاوی لینک تغییر کلمه عبور برای {user_username.first().email} ارسال شد.')

                return redirect('/')

        if not user_email.exists() or not user_username.exists():
            messages.warning(request, 'چنین ایمیلی موجود نمی باشد.')

    context = {

    }
    return render(request, 'forget-password.html', context)


def changing_password(request, token):
    changepassword_form = ChangePassword(request.POST or None)
    user = User.objects.filter(forgot_password_token__iexact=token)

    if not user.exists():
        raise Http404()
    elif user.exists():
        if user.first().time_created_token < timezone.now().date():
            raise Http404
        if request.method == 'POST':
            user_found = user.first()
            if changepassword_form.is_valid():
                print('12')
                password = changepassword_form.cleaned_data['password']
                user_found.set_password(password)
                user_found.forgot_password_token = ''
                user_found.save()
                messages.success(request, 'کلمه عبور با موفقیت تغییر کرد')
                return redirect('/')

    return render(request, 'change-password.html', {'changepassword_form': changepassword_form, 'token': token})


@login_required(login_url='/Login')
def my_courses(request):
    course = UsersBuysStatus.objects.filter(user=request.user).all()
    context = {
        'coursess': course
    }
    return render(request, 'mycourses.html', context)
