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
from mysite.api.items.plan import *
from .config import *

# Create your views here.


def record(request):
    
    username = request.session.get("username")
    user_permission={}
    user_list=['Z001','Z002','Z003','Z004','Z005','Z006','Z007','Z008','Z009','Z010']

    if username:
        if (username in user_list):       
            user_permission['user_permission']='Y'
        return render(request,'page/record.html',user_permission)
    else:
        return redirect('/login/')

        
#点检项目首页
def items(request):
    username = request.session.get("username")
    if username:
        ##20200514取消班组长以上修改点检项目的权限，设定为Z002
        # user_permission={}
        # user_level=zzuser.objects.filter(username=username).values('level')
        # user_permission['user_permission']=user_level[0]['level']

        #前端不变，只改变后端
        user_permission={}
        user_list=['Z001','Z002','Z003','Z004','Z005','Z006','Z007','Z008','Z009','Z010']
        if (username in user_list):
            user_permission['user_permission']='工段长'
        else:
            user_permission['user_permission']='班组长'        
        return render(request,'page/items.html',user_permission)
        
    else:
        return redirect('/login/')


#用户
def user(request):

    username = request.session.get("username")
    # user_list=['Z001','Z002','Z003','Z004','Z005','Z006','Z007','Z008','Z009','Z010']
    user_list=['Z001','Z002']
    if (username in user_list):
        return render(request,'page/user.html')
    elif(username):
        return HttpResponse('没有权限')
    else:
        return redirect('/login/')


#点检计划
def pc_plan(request):
    username = request.session.get("username")
    if username:
        return render(request,'page/plan.html')
    else:
        return redirect('/login/')

def login(request):
    return render(request,'page/login.html')


#布局图展示
def layout(request):
    return render(request,'page/layout.html')

#检查更新api
def checkupdate_api(request):
    date=app_vesion.objects.all().values()
    vesion=date[0]['appvesion']
    data={}
    data['vesion']=vesion
    return JsonResponse(data)


# def layout_test(request):
#     return render(request,'layout1.html')


def plan_test(request):
    return render(request,'plan1.html')

def index(request):
    username = request.session.get("username")
    if username:
        user_info={}
        user_info['username']=username
        return render(request,'index.html',user_info)
    else:
        return redirect('/login/')

def problem(request):
    username = request.session.get("username")
    test={}
    test['test']='22'
    if username:
        return render(request,'page/problem.html',test)
    else:
        return redirect('/login/')

def confirm(request):
    username = request.session.get("username")
    if username:
        user_level=zzuser.objects.filter(username=username).values('level')
        if(user_level[0]['level']=='班组长'):
            return HttpResponse('没有权限')
        else:
            return render(request,'page/confirm.html')
    else:
        return redirect('/login/')

def track(request):
    username = request.session.get("username")
    if username:
        user_permission={}
        user_level=zzuser.objects.filter(username=username).values('level')
        user_permission['user_permission']=user_level[0]['level']
        return render(request,'page/track.html',user_permission)
    else:
        return redirect('/login/')


def init_api(request):
    return JsonResponse(init_config)
def welcome(request):
    return render(request,'page/welcome.html')


def change_password(request):
    return render(request,'page/user-password.html')
#修改密码
def pc_change_password_api(request):
    username = request.session.get("username")
    old_password=request.POST.get('old_password')
    new_password=request.POST.get('new_password')
    print(old_password)
    res={}
    if username:
        date=zzuser.objects.filter(username=username).values('password')
        for i in date:
            if(i['password']==old_password):
                print(i['password'])
                zzuser.objects.filter(username=username).update(password=new_password)
                res['res']=1
            else:
                res['res']=2
    return JsonResponse(res)