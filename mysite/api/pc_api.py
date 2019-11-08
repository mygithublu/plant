from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from mysite.models import *
import datetime
import json




##点检项目获取
def items_pc_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    if(request.GET.get('workshop')or request.GET.get('worksection')or request.GET.get('team')or request.GET.get('level')or request.GET.get('shift')or request.GET.get('uloc')):
        workshop=request.GET.get('workshop')
        worksection=request.GET.get('worksection')
        team=request.GET.get('team')
        level=request.GET.get('level')
        shift=request.GET.get('shift')
        uloc=request.GET.get('uloc')
        
        search_info=dict()
        if workshop:
            search_info['workshop']=workshop
        if worksection:
            search_info['worksection']=worksection
        if team:
            search_info['team']=team            
        if level:
            search_info['level']=level
        if shift:
            search_info['shift']=shift
        if uloc:
            search_info['uloc']=uloc
        #通过字典方式查询，**dict   
        date=bas_title.objects.filter(**search_info)[s:e].values()
        count=bas_title.objects.filter(**search_info).count()
        data = {}
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)        
    else:
        date=bas_title.objects.all()[s:e].values()
        count=bas_title.objects.all().count()
        data = {}
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)

#点检记录删除
def record_delete_api(request):
    if(request.POST.get('data')):
        data=json.loads(request.POST.get('data'))
        print(data)
        for i in data:
            print(i['id'])
        return redirect('/index/')
    if(request.POST.get('id')):
        id=request.POST.get('id')
        print(id)
        return redirect('/index/')
#点检记录
def record_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    if(request.GET.get('workshop')or request.GET.get('worksection')or request.GET.get('team')or request.GET.get('level')or request.GET.get('shift')or request.GET.get('uloc')or request.GET.get('date') \
        or request.GET.get('res') or request.GET.get('username') or request.GET.get('name') ):
        workshop=request.GET.get('workshop')
        worksection=request.GET.get('worksection')
        team=request.GET.get('team')
        level=request.GET.get('level')
        shift=request.GET.get('shift')
        uloc=request.GET.get('uloc')
        date=request.GET.get('date')
        res=request.GET.get('res')
        username=request.GET.get('username')
        name=request.GET.get('name')
        search_info=dict()
        if workshop:
            search_info['workshop']=workshop
        if worksection:
            search_info['worksection']=worksection
        if team:
            search_info['team']=team            
        if level:
            search_info['level']=level
        if shift:
            search_info['shift']=shift
        if uloc:
            search_info['uloc']=uloc
        if date:
            search_info['date']=date
        if res:
            search_info['res']=res
        if username:
            search_info['username']=username
        if name:
            search_info['name']=name
        #获取数据条数
        date=record.objects.filter(**search_info)[s:e].values()
        data = {}
        count=record.objects.filter(**search_info).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data) 
    else:
        date=record.objects.all()[s:e].values()
        data = {}
        #获取数据条数
        count=record.objects.all().count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data)


def user_vue_api(request):

        #分页
    
    body=eval(str(request.body,encoding='utf-8'))
    page=body['page']
    size=body['size']
    print(page)
    print(body)
    s=(page-1)*size
    e=s+size
    date=zzuser.objects.all()[s:e].values()
    count=zzuser.objects.all().count()
    res={}
    res['res1']=list(date)
    res['total']=count
    return JsonResponse(res)


def test_api(request):
    res={}
    res['res']='0'
    return JsonResponse(res)

