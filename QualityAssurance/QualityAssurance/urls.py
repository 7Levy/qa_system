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
from qa_common.extensions import server_time
from qa_common import views
from qa_defect_management import views as view_defect
from qa_meeting_log import views as view_meeting
from qa_product_backlog import views as view_product
from qa_sprint_backlog import views as view_sprint
from qa_version_management import views as view_version
from qa_case import views as view_case
urlpatterns = [
    #公共模块
    path('api/time',server_time.GetCurrentTime.as_view()),
    path('api/login', views.Login.as_view()),
    re_path(r'^api/userhub/(?P<user>\w{1,8})$',views.UserHub.as_view()),
    path('api/v1/search',views.SearchUser.as_view()),
    #缺陷管理
    re_path(r'^api/bug/(?P<version_id>\w{1,8})$',view_defect.BugListView.as_view()),
    re_path(r'^api/bug/detail/(?P<bug_id>\w{1,8})$',view_defect.BugDetailView.as_view()),
    path('api/bug/management',view_defect.BugManageView.as_view()),
    # 用例管理
    re_path(r'^api/case/(?P<version_id>\w{1,8})$', view_case.CaseListView.as_view()),
    re_path(r'^api/case/detail/(?P<case_id>\w{1,8})$', view_case.CaseDetailView.as_view()),
    path('api/case/management', view_case.CaseManageView.as_view()),
    #版本管理
    path('api/version',view_version.VersionManagement.as_view()),


    #立会接口
    path('api/meeting/record',view_meeting.MeetingListView.as_view()),
    re_path(r'^api/meeting/record/detail/(?P<meeting_id>\w{1,8})$',view_meeting.MeetingDetailView.as_view()),
    path('api/meeting/record/management',view_meeting.MeetingManageView.as_view()),

    #产品订单
    path('api/product',view_product.ProductListView.as_view()),
    re_path(r'^api/product/detail/(?P<product_id>\w{1,8})$',view_product.ProductDeatilView.as_view()),
    re_path(r'^api/product/demand/detail/(?P<demand_id>\w{1,8})$',view_product.DemandDeatilView.as_view()),
    path('api/product/management',view_product.ProductManageView.as_view()),
    path('api/product/demand/management',view_product.ProductDemandView.as_view()),

    #冲刺订单
    path('api/sprint', view_sprint.SprintListView.as_view()),
    re_path(r'^api/sprint/detail/(?P<sprint_id>\w{1,8})$', view_sprint.SprintDeatilView.as_view()),
    re_path(r'^api/sprint/demand/detail/(?P<demand_id>\w{1,8})$', view_sprint.DemandDeatilView.as_view()),
    path('api/sprint/management', view_sprint.SprintManageView.as_view()),
    path('api/sprint/demand/management', view_sprint.SprintDemandView.as_view()),

]
