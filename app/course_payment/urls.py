from django.urls import path

from course_payment import views

urlpatterns = [
    path('payment/<int:cId>', views.go_to_gateway_view),
    path('callback-gateway/<int:cId>', views.callback_gateway_view)
]
