"""Course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from azbankgateways.urls import az_bank_gateways_urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
import Course_home
from Course import settings

urlpatterns = [
    path('my_ultra_admin/', admin.site.urls),
    path('', include('Course_home.urls')),
    path('', include('course_account.urls')),
    path('', include('User.urls')),
    path('', include('course_payment.urls')),
    path('', include('courses_videos.urls')),
    path('', include('course_comments.urls')),
    path('', include('social_django.urls', namespace='social')),
    url(r'^tinymce/', include('tinymce.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
