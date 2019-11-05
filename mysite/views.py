from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from mysite.models import zzuser,bas_title,record
import datetime
import json
from mysite.api.app_api import *
from mysite.api.pc_api import *
from mysite.api.user.user_api import *
from mysite.api.login.login_api import *
from mysite.api.layout.layout_api import *
from mysite.api.items.items_api import *


# Create your views here.


def record(request):
    
    username = request.session.get("username")
    if username:
        return render(request,'record.html')
    else:
        return redirect('/login/')

        
#点检项目首页
def items(request):
    username = request.session.get("username")
    if username:
        return render(request,'items.html')
    else:
        return redirect('/login/')


#用户
def user(request):

    username = request.session.get("username")
    if username:
        return render(request,'user.html')
    else:
        return redirect('/login/')


#点检计划
def pc_plan(request):
    username = request.session.get("username")
    if username:
        return render(request,'plan.html')
    else:
        return redirect('/login/')

def login(request):
    return render(request,'login.html')


#布局图展示
def layout(request):
    return render(request,'layout.html')

#检查更新api
def checkupdate_api(request):
    date=app_vesion.objects.all().values()
    vesion=date[0]['appvesion']
    data={}
    data['vesion']=vesion
    return JsonResponse(data)

    