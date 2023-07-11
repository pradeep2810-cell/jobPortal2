"""job_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import os.path

import ckeditor_uploader.urls
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from information import views
from job_portal import settings
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor_upload/', include(ckeditor_uploader.urls.urlpatterns)),

    # http://127.0.0.1:8000/
    path('', views.show_home, name='home'),

    path('account/', include('accounts.urls')),
    path('info/', include('information.urls')),
    path('jobs/', include('jobs.urls')),
    # path('organizations/', include('organizations.urls')),
    # path('jobseekers/', include('jobseekers.urls')),
    path('applications/', include('applications.urls')),

    path('api/', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
