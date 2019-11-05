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
    url(r'record_delete_api',record_delete_api),
    url(r'record/',record),
    url(r'items_pc_api',items_pc_api),
    url(r'items/',items),
    url(r'user_pc_api',user_pc_api),
    url(r'user/',user),
    url(r'plan/',pc_plan),
    url(r'login/',login),
    url(r'user_vue_api',user_vue_api),
    url(r'add_user_api',add_user_api),
    url(r'edit_user_api',edit_user_api),
    url(r'pc_login_api',pc_login_api),
    url(r'layout/',layout),
    url(r'test_api',test_api),
    url(r'user_delete_api',user_delete_api),
    url(r'user_upload_file',user_upload_file),
    url(r'user_templates_download',user_templates_download),
    url(r'layout_res_api',layout_res_api),
    url(r'item_upload_file/',item_upload_file),
    url(r'item_templates_download/',item_templates_download),
    url(r'item_delete_api',item_delete_api),
    url(r'edit_item_api',edit_item_api),
    url(r'checkupdate_api',checkupdate_api),
]
