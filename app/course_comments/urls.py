from django.urls import path

from course_comments import views

urlpatterns = [
    path('comments', views.comments_part, name='comments')
]
