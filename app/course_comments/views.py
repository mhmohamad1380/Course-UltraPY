from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from course_comments.forms import CommentForm
from course_comments.models import Comments


@login_required(login_url='/Login')
def comments_part(request):

    context = {
    }
    return render(request, 'comments.html', context)
