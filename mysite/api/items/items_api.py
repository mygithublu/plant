from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from mysite.models import *
import datetime
import json
import pandas as pd
from django.http import FileResponse #文件下载


#上传
#点检导入导入并创建
def item_upload_file(request):
    #接收文件到服务器
    myFile = request.FILES.get('myfile', None)         
    excelFile = open('D:/plant/upload/item/'+ myFile.name, 'wb+')
    for chunk in myFile.chunks():
        excelFile.write(chunk)
        excelFile.close()
    #创建用户
    df=pd.read_excel('D:/plant/upload/item/'+ myFile.name)
    #替换nan值为空字符串
    df=df.fillna('')
    row=df.shape[0]
    item_info=dict()
    today=datetime.date.today()
    for i in range(row):
        workshop=df.iloc[i,0]
        worksection=df.iloc[i,1]
        team=df.iloc[i,2]
        level=df.iloc[i,3]
        shift=df.iloc[i,4]
        uloc=df.iloc[i,5]
        title=df.iloc[i,6]

        item_info['workshop']=df.iloc[i,0]
        item_info['worksection']=df.iloc[i,1]
        item_info['team']=df.iloc[i,2]       
        item_info['level']=df.iloc[i,3]       
        item_info['shift']=df.iloc[i,4]       
        item_info['uloc']=df.iloc[i,5]                     
        item_info['title']=df.iloc[i,6]
        is_plan=plan_status.objects.filter(workshop=workshop,worksection=worksection,team=team,level=level,shift=shift,uloc=uloc,date__gte=today)\
            .values('plan_id','workshop','worksection','team','level','shift','uloc','date')\
            .order_by('plan_id','workshop','worksection','team','level','shift','uloc','date').distinct()
        #点检状态表里面当前工位 是否存在大于等于当前日期的，如果存在，则创建状态表
        if is_plan:
            bas_title.objects.create(**item_info)
            #通过当前最大id，找到当前创建的数据
            cur=bas_title.objects.latest('id')
            cur_id=cur.id
            is_plan=list(is_plan)
            for i in is_plan:
                plan_status.objects.create(item_id=cur_id,plan_id=i['plan_id'],workshop=i['workshop'],worksection=i['worksection'],team=i['team'],level=i['level'],shift=i['shift'],uloc=i['uloc'],title=title,date=i['date'],status='0')
            #创建完毕后，把创建信息置为空
            item_info=dict()
        else:
            bas_title.objects.create(**item_info)
            #创建完毕后，把创建信息置为空
            item_info=dict()
    res = {}
    res['res'] = 'ok'
    return JsonResponse(res)  



#模板下载
def item_templates_download(request):
    file=open('D:/plant/templates/items.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="items.xlsx"'
    return response


#删除
def item_delete_api(request):
    today=datetime.date.today()
    #批量删除
    if(request.POST.get('data')):
        data=json.loads(request.POST.get('data'))
        print(data)
        for i in data:
            id=i['id']
            #大于等于当前日期存在计划，则不能删除
            is_plan=plan_status.objects.filter(item_id=id,date__gte=today).values()
            if is_plan:
                print('大于等于当前日期有点检计划，请先删除点检计划')
            else:
                print('!!!')
                bas_title.objects.filter(id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    if(request.POST.get('id')):
        id=request.POST.get('id')
        print(id)
        #大于等于当前日期存在计划，则不能删除
        is_plan=plan_status.objects.filter(item_id=id,date__gte=today).values()
        if is_plan:
            res = {}
            res['res'] = '大于等于当前日期有点检计划，请先删除点检计划'
            return JsonResponse(res) 
        else:
            bas_title.objects.filter(id=id).delete()
            res = {}
            res['res'] = 'ok'
            return JsonResponse(res)

#更新
def edit_item_api(request):
    today=datetime.date.today()
    id=request.POST.get('id')
    post_title=request.POST.get('title')
    title=bas_title.objects.filter(id=id).values()
    title=title[0]['title']
    #如果没有修改
    if(post_title==title):
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    else:
        
        is_plan=plan_status.objects.filter(item_id=id,date__gte=today).values()
        #大于等于当前日期存在计划，则更新大于等于当前日期的状态表，并置为0
        if is_plan:
            plan_status.objects.filter(item_id=id,date__gte=today,status='0')
            res = {}
            res['res'] = 'ok'
            return JsonResponse(res)
        else:
            bas_title.objects.filter(id=id).update(title=title)
            res = {}
            res['res'] = 'ok'
            return JsonResponse(res)



#新增
def add_item_api(request):
    today=datetime.date.today()
    workshop=request.POST.get('workshop')
    worksection=request.POST.get('worksection')
    team=request.POST.get('team')
    level=request.POST.get('level')
    shift=request.POST.get('shift')
    uloc=request.POST.get('uloc')
    title=request.POST.get('title')

    add_info=dict()    
    add_info['workshop']=request.POST.get('workshop')
    add_info['worksection']=request.POST.get('worksection')
    add_info['team']=request.POST.get('team')
    add_info['level']=request.POST.get('level')
    add_info['shift']=request.POST.get('shift')
    add_info['uloc']=request.POST.get('uloc')
    add_info['title']=request.POST.get('title')

    is_plan=plan_status.objects.filter(workshop=workshop,worksection=worksection,team=team,level=level,shift=shift,uloc=uloc,date__gte=today)\
        .values('plan_id','workshop','worksection','team','level','shift','uloc','date')\
        .order_by('plan_id','workshop','worksection','team','level','shift','uloc','date').distinct()
    #点检状态表里面当前工位 是否存在大于等于当前日期的，如果存在，则创建状态表
    if is_plan:
        bas_title.objects.create(**add_info)
        #通过当前最大id，找到当前创建的数据
        cur=bas_title.objects.latest('id')
        cur_id=cur.id
        is_plan=list(is_plan)
        for i in is_plan:
            plan_status.objects.create(item_id=cur_id,plan_id=i['plan_id'],workshop=i['workshop'],worksection=i['worksection'],team=i['team'],level=i['level'],shift=i['shift'],uloc=i['uloc'],title=title,date=i['date'],status='0')
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)  
    else:
        bas_title.objects.create(**add_info)
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)  

