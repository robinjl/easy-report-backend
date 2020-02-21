"""easyreport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from users.views import UserViewSet
from reports.views import DailyReportViewSet, WeeklyReportViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='用户')
router.register(r'daily-report', DailyReportViewSet, basename='日报')
router.register(r'weekly-report', WeeklyReportViewSet, basename='周报')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'doc/', include_docs_urls(title='日报小程序API')),
    path(r'', include(router.urls)),
]
