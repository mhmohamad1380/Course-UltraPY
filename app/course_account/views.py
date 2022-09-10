from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from Course_home.models import Course
from User.models import User
from .forms import LoginForms, RegisterForms
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .models import FavoriteCourses


def login_view(request):
    print(request.GET)
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForms(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        auth_check = authenticate(username=username, password=password)
        if auth_check:
            login(request, auth_check)
            login_form = LoginForms()

            return redirect('/')
        else:
            login_form.add_error('username', 'نام کاربری یا کلمه عبور اشتباه می باشد')
    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(request.GET.get('next'))
    return HttpResponseRedirect(request.GET.get('next'))


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForms(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data['username']
        email = register_form.cleaned_data['email']
        password = register_form.cleaned_data['password']
        re_password = register_form.cleaned_data['re_password']

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/Login')
    context = {
        'register_form': register_form
    }
    return render(request, 'Register.html', context)


@login_required(login_url='/Login')
def add_to_favorite(request, cId):
    course = Course.objects.get(id=cId)
    if not FavoriteCourses.objects.filter(user=request.user, favorite_courses=course).exists():
        FavoriteCourses.objects.create(user=request.user, favorite_courses=course)
    return redirect(request.GET.get('next'))


@login_required(login_url='/Login')
def delete_from_favorite(request, cId):
    course = FavoriteCourses.objects.filter(user=request.user, favorite_courses__id=cId)
    if course.exists():
        course.delete()
    return redirect(request.GET.get('next'))


@login_required(login_url='/Login')
def favorites(request):
    favs:FavoriteCourses = FavoriteCourses.objects.filter(user=request.user).all()
    context = {
        'courses': favs
    }
    return render(request, 'favorites.html', context)
