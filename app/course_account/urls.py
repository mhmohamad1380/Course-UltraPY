from django.urls import path

from course_account import views

urlpatterns = [
    path('Login', views.login_view),
    path('logout', views.log_out),
    path('Register', views.register_view),
    path('AddtoFavorite/<int:cId>', views.add_to_favorite),
    path('DeletefromFavorite/<int:cId>', views.delete_from_favorite),
    path('Favorites', views.favorites)
]
