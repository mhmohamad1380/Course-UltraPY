from django.urls import path

from courses_videos import views

urlpatterns = [
    path('UploadFile/<int:sessionId>/<int:courseId>', views.uploadfile),
    path('CreateSession/<int:courseId>', views.create_session),
]
