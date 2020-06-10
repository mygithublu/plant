"""plant URL Configuration

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
from django.urls import path
from django.conf.urls import url
from mysite.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^submit_api/',submit_api),
    url(r'^login_api',login_api),
    url(r'get_title_api/',get_title_api),
    url(r'record_api/',record_api),
    url(r'get_title_api',get_title_api),
    url(r'^get_plan_status_api',get_plan_status_api),
    url(r'^record__download',record__download),
    url(r'record_delete_api',record_delete_api),
    url(r'^index/record/$',record),
    url(r'items_pc_api',items_pc_api),
    url(r'^index/items/$',items),
    url(r'user_pc_api',user_pc_api),
    url(r'^index/user/$',user),
    url(r'^index/pc_plan/$',pc_plan),
    url(r'^login/$',login),
    url(r'user_vue_api',user_vue_api),
    url(r'add_user_api',add_user_api),
    url(r'edit_user_api',edit_user_api),
    url(r'pc_login_api',pc_login_api),
    url(r'^index/layout/$',layout),
    url(r'test_api',test_api),
    url(r'user_delete_api',user_delete_api),
    url(r'user_upload_file',user_upload_file),
    url(r'user_templates_download',user_templates_download),
    url(r'layout_res_api',layout_res_api),
    #点检项
    url(r'item_upload_file/',item_upload_file),
    url(r'add_item_api',add_item_api),
    url(r'item_templates_download/',item_templates_download),
    url(r'item_delete_api',item_delete_api),
    url(r'edit_item_api',edit_item_api),
    url(r'checkupdate_api',checkupdate_api),
    #plan
    url(r'plan_upload_file',plan_upload_file),
    url(r'plan_templates_download',plan_templates_download),
    url(r'plan_delete_api',plan_delete_api),
    url(r'edit_plan_api',edit_plan_api),
    url(r'add_plan_api',add_plan_api),
    url(r'pc_plan_api',pc_plan_api),
    # url(r'layout_test/',layout_test),
    url(r'plan_test/',plan_test),
    url(r'p_tt_api',p_tt_api),

    #主页
    url(r'index/$',index),
    url(r'^index/init_api/$',init_api),
    url(r'^index/welcome/$',welcome),
    url(r'^change_password/$',change_password),
    url(r'^pc_change_password_api/$',pc_change_password_api),

    #问题管理
    url(r'^index/problem/$',problem),
    url(r'pc_problem_api',pc_problem_api),
    url(r'^index/confirm/$',confirm),
    url(r'pc_confirm_api',pc_confirm_api),
    url(r'^index/track/$',track),
    url(r'pc_track_api',pc_track_api),
    url(r'^edit_problem_api/$',edit_problem_api),
    url(r'^delete_problem_api$',delete_problem_api),
    url(r'^edit_confirm_api',edit_confirm_api),
]
