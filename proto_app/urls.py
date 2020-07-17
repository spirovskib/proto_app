"""proto_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include,re_path

from django.conf.urls.static import static
from django.conf import settings

from application.views import home_view, view_post_detail, new_post_view, new_project_view, project_detail_view, err_handler403, err_handler404
from accounts.views import profile_view, profile_user_view, manage_users_view, add_user_project_view

handler403 = err_handler403
handler404 = err_handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_view, name='home'),
    path('view_post/<slug:slug>', view_post_detail, name='view_post'),
    path('new_post/<slug:slug>', new_post_view, name='new_post'),
    path('profile/', profile_view, name='profile_view'), # IMPORTANT - NOT FINISHED
    path('profile/<slug:slug>', profile_user_view, name='profile_user_view'), # IMPORTANT - NOT FINISHED
    path('project/', new_project_view, name='new_project'),
    path('project/<slug:slug>', project_detail_view, name='project_detail'),   
    path('add_user_project/<slug:slug>', add_user_project_view, name='add_user_project'),   
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
