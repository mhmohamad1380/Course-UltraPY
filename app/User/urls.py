from django.urls import path

from User import views

urlpatterns = [
    path('forget-password', views.forget_password_view),
    path('forget-password/tokenId=<token>', views.changing_password),
    path('Account/My-Courses', views.my_courses)
]
