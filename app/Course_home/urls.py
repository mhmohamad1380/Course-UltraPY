from django.urls import path

from Course_home import views

urlpatterns = [
    path('', views.homepage),
    path('Courses-List', views.CourseView.as_view()),
    path('Courses-List/<int:Id>/<str:Cname>', views.course_detail),
    path('media/Course_Videos/<str:title>', views.videos_view),
    path('downloadvideo/<int:videoId>/course_id=<int:courseId>', views.download_video),
    path('delete_session/<int:sId>', views.delete_session),
    path('freecourse/buy/<int:cId>', views.buy_free_course)

]
