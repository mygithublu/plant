from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from mysite.models import *
import datetime
import json

def layout_res_api(request):
    today=datetime.date.today()
    #找到当天，状态为0，代表没有点检完成，红色状态
    no_check=bas_title.objects.filter(date=today,status='0').values('worksection','team','shift')\
        .order_by('worksection','team','shift').distinct()

    #找到当天，所有NOK的结果
    nook_check=record.objects.filter(date=today,res='NOK').values('worksection','team','shift')\
        .order_by('worksection','team','shift').distinct()
    no_check=list(no_check)
    nook_check=list(nook_check)
    #通过循环，去掉NOK里面没有完成的班组，筛选出点检完成但是有NOK的项，设置为黄色
    for i in no_check:
        for p in nook_check:
            if i==p:
              nook_check.remove(p)
    status=[]
    for i in no_check:
        i['team_status']='red'
        
    for i in nook_check:
         i['team_status']='yellow' 

    status=no_check+nook_check      
    print(status)   
    data={}
    data['res']=status
    return JsonResponse(data)
