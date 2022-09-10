from Course_home.models import Course
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_confirmation_mail(user_email, course_id):
    course = Course.objects.filter(id=course_id)
    send_mail("دوره ی جدید با موفقیت خریداری شد", f"شما با موفقیت دوره ی {course.name} را خریداری کردید",
              "ultrapy.education@gmail.com", [user_email])