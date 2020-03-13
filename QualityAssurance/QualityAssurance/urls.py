"""QualityAssurance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path,include
from qa_common import views
from qa_defect_management import views as view_defect
urlpatterns = [
    path('api/v1/login', views.Login.as_view()),
    re_path(r'^api/v1/userhub/(?P<user>\w{1,8})$',views.UserHub.as_view()),
    path('api/v1/search',views.SearchUser.as_view()),
    re_path(r'^api/v1/buglist/(?P<version_id>\w{1,8})$',view_defect.BugListView.as_view()),
    re_path(r'^api/v1/bugdetail/(?P<bug_id>\w{1,8})$',view_defect.BugDetailView.as_view())
]
