from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from mysite.models import *
import datetime
import json


def pc_login_api(request):
    #用户登录api
    username=request.POST.get('username')
    password=request.POST.get('password')
    ok=zzuser.objects.filter(username=username,password=password).values()
    if(ok):
        if(ok[0]['is_admin']=='是'):
            res={}
            res['res']=1
            res['username']=username
            request.session["username"] = ok[0]['username']
            request.session.set_expiry(60*60)
            return JsonResponse(res)
        else:
            res={}
            res['res']=2 
            request.session.set_expiry(60*30)
            return JsonResponse(res)
    else:
        res={}
        res['res']=0
        return JsonResponse(res)        