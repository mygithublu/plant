from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from mysite.models import *
import datetime
import json
import pandas as pd
from django.http import FileResponse #文件下载
from mysite.config import user_info_hs
#上传
#点检导入导入并创建
def plan_upload_file(request):
    #接收文件到服务器
    myFile = request.FILES.get('myfile', None)         
    excelFile = open('./upload/plan/'+ myFile.name, 'wb+')
    for chunk in myFile.chunks():
        excelFile.write(chunk)
        excelFile.close()
    #创建用户
    df=pd.read_excel('./upload/plan/'+ myFile.name)
    #替换nan值为空字符串
    df=df.fillna('')
    row=df.shape[0]
    plan_info=dict()
    for i in range(row):
        workshop=df.iloc[i,0]
        worksection=df.iloc[i,1]
        team=df.iloc[i,2]
        level=df.iloc[i,3]
        shift=df.iloc[i,4]
        uloc=df.iloc[i,5]
        date=df.iloc[i,6]   
        plan_info['workshop']=df.iloc[i,0]
        plan_info['worksection']=df.iloc[i,1]
        plan_info['team']=df.iloc[i,2]       
        plan_info['level']=df.iloc[i,3]       
        plan_info['shift']=df.iloc[i,4]        
        plan_info['uloc']=df.iloc[i,5]                             
        plan_info['date']=df.iloc[i,6]
        #相同工位，相同日期，相同班次等是否存在
        is_exist=pc_plan.objects.filter(**plan_info).values()
        if is_exist:
            res = {}
            res['res'] = '相同数据已经存在'
           
        else:
            #是否存在点检项目
            is_item=bas_title.objects.filter(workshop=workshop,worksection=worksection,team=team,level=level,shift=shift,uloc=uloc).values()              
            if is_item:
                pc_plan.objects.create(**plan_info)
                cur_date=pc_plan.objects.filter(**plan_info).values()
                plan_id=cur_date[0]['id']
                is_item=list(is_item)
                print(is_item)
                for o in is_item:
                     #20200117新增类别，维度，分类字段
                    plan_status.objects.create(plan_id=plan_id,item_id=o['id'],title=o['title'],title_lb=o['title_lb'],title_wd=o['title_wd'],title_fl=o['title_fl'],workshop=workshop,worksection=worksection,team=team,level=level,shift=shift,uloc=uloc,date=date,status='0')
                plan_info=dict()
            else:
                res = {}
                res['res'] = '此工位未维护点检项目，无法创建计划'

    data = {}
    data['code']=0
    data['msg']=""
    data['data']='ok'
    return JsonResponse(data)


#模板下载
def plan_templates_download(request):
    # file=open('D:/plant/templates/plan.xlsx','rb')
    file=open('./templates/plan.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="plan.xlsx"'
    return response


#删除
def plan_delete_api(request):
    #批量删除
    if(request.POST.get('data')):
        data=json.loads(request.POST.get('data'))
        print(data)
        for i in data:
            id=i['id']
            pc_plan.objects.filter(id=id).delete()
            #删除点检状态表
            plan_status.objects.filter(plan_id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    if(request.POST.get('id')):
        id=request.POST.get('id')
        print(id)
        #删除计划表
        pc_plan.objects.filter(id=id).delete()
        #删除点检状态表
        plan_status.objects.filter(plan_id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)

#更新
def edit_plan_api(request):
    id=request.POST.get('id')
    workshop=request.POST.get('workshop')
    worksection=request.POST.get('worksection')
    team=request.POST.get('team')
    level=request.POST.get('level')
    shift=request.POST.get('shift')
    uloc=request.POST.get('uloc')
    date=request.POST.get('date')

    cur_id=pc_plan.objects.filter(id=id).values()
    cur_id=cur_id[0]['date']
    #日期转换为字符串
    cur_id=cur_id.strftime('%Y-%m-%d')
    print(type(cur_id))
    print(type(date))
    if (date==cur_id):
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    else:
        update_info=dict()    
        update_info['workshop']=request.POST.get('workshop')
        update_info['worksection']=request.POST.get('worksection')
        update_info['team']=request.POST.get('team')
        update_info['level']=request.POST.get('level')
        update_info['shift']=request.POST.get('shift')
        update_info['uloc']=request.POST.get('uloc')
        update_info['date']=request.POST.get('date')
        #相同工位，相同日期是否存在
        is_exist=pc_plan.objects.filter(**update_info).values()
        if is_exist:
            res = {}
            res['res'] = '相同数据已经存在'
            print(res)
            return JsonResponse(res)
        else:
            pc_plan.objects.filter(id=id).update(date=date)
            #修改点检状态表,并把状态置为0
            plan_status.objects.filter(plan_id=id).update(date=date,status='0')
            res = {}
            res['res'] = 'ok'
            return JsonResponse(res)   

  


#新增
def add_plan_api(request):
    add_info=dict()
    workshop=request.POST.get('workshop')
    worksection=request.POST.get('worksection')
    team=request.POST.get('team')
    level=request.POST.get('level')
    shift=request.POST.get('shift')
    uloc=request.POST.get('uloc')
    date=request.POST.get('date')
    add_info['workshop']=request.POST.get('workshop')
    add_info['worksection']=request.POST.get('worksection')
    add_info['team']=request.POST.get('team')
    add_info['level']=request.POST.get('level')
    add_info['shift']=request.POST.get('shift')    
    add_info['uloc']=request.POST.get('uloc')    
    add_info['date']=request.POST.get('date')
    print(add_info)
    #相同工位，相同日期是否存在
    is_exist=pc_plan.objects.filter(**add_info).values()
    if is_exist:
        res = {}
        res['res'] = '相同数据已经存在'
        print(res)
        return JsonResponse(res)
    else:
        #是否存在点检项目，如果不存在则创建    
        is_item=bas_title.objects.filter(workshop=workshop,worksection=worksection,team=team,level=level,shift=shift,uloc=uloc).values()                    
        if is_item:
            pc_plan.objects.create(**add_info)
            cur_date=pc_plan.objects.filter(**add_info).values()
            plan_id=cur_date[0]['id']
            is_item=list(is_item)
            for o in is_item:
                plan_status.objects.create(plan_id=plan_id,item_id=o['id'],title=o['title'],title_lb=o['title_lb'],title_wd=o['title_wd'],title_fl=o['title_fl'],workshop=workshop,worksection=worksection,team=team,level=level,shift=shift,uloc=uloc,date=date,status='0')
            res = {}
            res['res'] = 'ok'
            return JsonResponse(res)   
        else:
            res = {}
            res['res'] = '未维护点检项目，无法创建计划'
            print(res)
            return JsonResponse(res)    




##点检计划获取
def pc_plan_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    username = request.session.get("username")
    data_info=user_info_hs(username)
    if(request.GET.get('workshop')or request.GET.get('worksection')or request.GET.get('team')or request.GET.get('level')or request.GET.get('shift')or request.GET.get('uloc')or request.GET.get('date')):
        workshop=request.GET.get('workshop')
        worksection=request.GET.get('worksection')
        team=request.GET.get('team')
        level=request.GET.get('level')
        shift=request.GET.get('shift')
        uloc=request.GET.get('uloc')
        date=request.GET.get('date')
        search_info=dict()
        if workshop:
            if 'workshop' in data_info :
                search_info['workshop']=data_info['workshop']
                del data_info['workshop']
            else:                
                search_info['workshop']=workshop
        if worksection:
            if 'worksection' in data_info :
                search_info['worksection']=data_info['worksection']
                del data_info['worksection']
            else:
                search_info['worksection']=worksection
        if team:
            if 'team' in data_info :
                search_info['team']=data_info['team']
                del data_info['team']
            else:
                search_info['team']=team                
        if level:
            if 'level' in data_info:                
                search_info['level']=data_info['level']
                del data_info['level']
            else:
                search_info['level']=level
        if shift:
            if 'shift' in data_info:                
                search_info['shift']=data_info['shift']
                del data_info['shift']
            else:
                search_info['shift']=shift
        if uloc:
            search_info['uloc']=uloc
        if date:
            #20200514修改为时间范围
            startime= date[0:10]
            endtime=date[-10:]
 
            # search_info['date']=date
            #通过字典方式查询，**dict   
            date=pc_plan.objects.filter(**search_info,**data_info,date__range=(startime,endtime))[s:e].values()
            count=pc_plan.objects.filter(**search_info,**data_info,date__range=(startime,endtime)).count()
            data = {}
            data['code']=0
            data['msg']=""
            data['count']=count
            data['data']=list(date)
            return JsonResponse(data)
        else:
            date=pc_plan.objects.filter(**search_info,**data_info)[s:e].values()
            count=pc_plan.objects.filter(**search_info,**data_info).count()
            data = {}
            data['code']=0
            data['msg']=""
            data['count']=count
            data['data']=list(date)
            return JsonResponse(data)

    else:
        date=pc_plan.objects.filter(**data_info)[s:e].values()
        count=pc_plan.objects.filter(**data_info).count()
        data = {}
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)


def p_tt_api(request):
    date=[{'day1':'N','day2':'N','day3':'Y','day4':'N','day5':'Y','day6':'N','day7':'N','today':'3'}]
    print(date)
    data = {}
    data['code']=0
    data['msg']=""
    data['count']=1
    data['data']=date
    
    return JsonResponse(data) 