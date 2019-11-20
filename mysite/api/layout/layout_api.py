from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from mysite.models import *
import datetime
import json

def layout_res_api(request):

    #从前台获取选择的日期和班次
    today=request.POST.get('select_date')
    shift=request.POST.get('select_shift')


    #默认当天
    # today=datetime.date.today()

  
    #所有工位的点检计划
    all_check=plan_status.objects.filter(date=today).values('worksection','team','shift')\
        .order_by('worksection','team','shift').distinct()
    #找到当天，状态为0，代表没有点检完成，红色状态
    no_check=plan_status.objects.filter(date=today,status='0').values('worksection','team','shift')\
        .order_by('worksection','team','shift').distinct()

    #找到当天，所有NOK的结果
    nook_check=record.objects.filter(date=today,res='NOK').values('worksection','team','shift')\
        .order_by('worksection','team','shift').distinct()
    no_check=list(no_check)
    nook_check=list(nook_check)
    all_check=list(all_check)
    #通过循环，去掉NOK里面没有完成的班组，筛选出点检完成但是有NOK的项，设置为黄色
    y1=[]
    for i in nook_check:
        if i not in no_check:
            y1.append(i)
    nook_check=y1
    #两次循环去掉红色和黄色的，留下绿色   

    t1=[]
    for i in all_check:
        
        if i not in no_check:
            t1.append(i)
        
    green_check=[]
    for i in t1:
        
        if i not in nook_check:
            green_check.append(i)

    status=[]
    for i in no_check:
        i['team_status']='red'
        
    for i in nook_check:
         i['team_status']='yellow' 

    
    for i in green_check:
        i['team_status']='green'
    
    #汇总所有班组的信息
    status=no_check+nook_check+green_check

    #筛选前台选择的班次
    select_status=[]
    for i in status:
        if (i['shift']==shift):
            select_status.append(i)


    print(select_status)
    data={}
    data['res']=select_status
    return JsonResponse(data)
