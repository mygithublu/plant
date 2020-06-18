from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from mysite.models import *
import datetime
import json
import pandas as pd
from django.http import FileResponse #文件下载



def user_pc_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    #如果有查询条件，则进行查询       
    if(request.GET.get('username')or request.GET.get('psn')or request.GET.get('workshop') or request.GET.get('worksection') or request.GET.get('shift') or request.GET.get('level') or request.GET.get('uloc') ):   
        search_info=dict()
        username=request.GET.get('username')
        psn=request.GET.get('psn')
        workshop=request.GET.get('workshop')
        worksection=request.GET.get('worksection')
        shift=request.GET.get('shift')
        level=request.GET.get('level')
        uloc=request.GET.get('uloc')
        if username:
            search_info['username']=username
        if psn:
            search_info['psn']=psn
        if workshop:
            search_info['workshop']=workshop
        if worksection:
            search_info['worksection']=worksection            
        if shift:
            search_info['shift']=shift   
        if level:
            search_info['level']=level   
        if uloc:
            search_info['uloc']=uloc
        #通过字典方式查询，**dict   
        date=zzuser.objects.filter(**search_info)[s:e].values()
        count=zzuser.objects.filter(**search_info).count()
        data = {}
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)        
    else:
        date=zzuser.objects.all()[s:e].values()
        count=zzuser.objects.all().count()
        data = {}
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)



def add_user_api(request):
    name = request.POST.get('name')
    psn = request.POST.get('psn')
    username = request.POST.get('username')
    worksection = request.POST.get('worksection')
    uloc = request.POST.get('uloc')
    workshop = request.POST.get('workshop')
    team = request.POST.get('team')
    shift = request.POST.get('shift')
    level = request.POST.get('level')
    is_admin=request.POST.get('is_admin')
    add_info=dict()
    if name:
        add_info['name']=name
    if psn:
        add_info['psn']=psn
    if username:
        add_info['username']=username
    if worksection:
        add_info['worksection']=worksection
    if uloc:
        add_info['uloc']=uloc
    if workshop:
        add_info['workshop']=workshop
    if team:
        add_info['team']=team
    if shift:
        add_info['shift']=shift
    if level:
        add_info['level']=level
    if is_admin:
        add_info['is_admin']=is_admin
    add_info['password']='123456'
    state = zzuser.objects.create(**add_info)
    res = {}
    res['res'] = 'ok'
    return JsonResponse(res)


def edit_user_api(request):
    id = request.POST.get('id')
    psn = request.POST.get('psn')
    name = request.POST.get('name')
    username = request.POST.get('username')
    workshop = request.POST.get('workshop')
    worksection = request.POST.get('worksection')
    uloc = request.POST.get('uloc')
    shift = request.POST.get('shift')
    level = request.POST.get('level')
    team = request.POST.get('team')
    is_admin=request.POST.get('is_admin')
    
    zzuser.objects.filter(id=id).update(psn=psn,name=name,username=username,workshop=workshop,worksection=worksection,uloc=uloc,shift=shift,level=level,team=team,is_admin=is_admin)
    res = {}
    res['res'] = 'ok'
    return JsonResponse(res)

def user_delete_api(request):
    #批量删除
    if(request.POST.get('data')):
        data=json.loads(request.POST.get('data'))
        print(data)
        for i in data:
            id=i['id']
            zzuser.objects.filter(id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    if(request.POST.get('id')):
        id=request.POST.get('id')
        print(id)
        zzuser.objects.filter(id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)


#上传
#用户导入并创建
def user_upload_file(request):
    #接收文件到服务器
    myFile = request.FILES.get('myfile', None)         
    excelFile = open('./upload/user/'+ myFile.name, 'wb+')
    for chunk in myFile.chunks():
        excelFile.write(chunk)
        excelFile.close()
    #创建用户
    df=pd.read_excel('./upload/user/'+ myFile.name)
    #替换nan值为空字符串
    df=df.fillna('')
    row=df.shape[0]
    user_info=dict()
    for i in range(row):
        user_info['username']=df.iloc[i,0]
        user_info['psn']=df.iloc[i,1]
        user_info['name']=df.iloc[i,2]
        user_info['workshop']=df.iloc[i,3]
        user_info['worksection']=df.iloc[i,4]
        user_info['team']=df.iloc[i,5]
        user_info['shift']=df.iloc[i,6]
        user_info['level']=df.iloc[i,7]
        user_info['uloc']=df.iloc[i,8]
        user_info['is_admin']=df.iloc[i,9]
        user_info['password']='123456'     
        zzuser.objects.create(**user_info)
        user_info=dict()

    data = {}
    data['code']=0
    data['msg']=""
    data['data']='ok'
    return JsonResponse(data)



def user_templates_download(request):
    # file=open('D:/plant/templates/user.xlsx','rb')
    file=open('./templates/user.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="user.xlsx"'
    return response