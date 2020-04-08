from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from mysite.models import *
import datetime
import json
import time
from mysite.config import user_info_hs


##点检项目获取
def items_pc_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    username = request.session.get("username")
    data_info=user_info_hs(username)
    if(request.GET.get('workshop')or request.GET.get('worksection')or request.GET.get('team')or request.GET.get('level')or request.GET.get('shift')or request.GET.get('uloc')):
        workshop=request.GET.get('workshop')
        worksection=request.GET.get('worksection')
        team=request.GET.get('team')
        level=request.GET.get('level')
        shift=request.GET.get('shift')
        uloc=request.GET.get('uloc')
        
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
        #通过字典方式查询，**dict   
        date=bas_title.objects.filter(**search_info,**data_info)[s:e].values()
        count=bas_title.objects.filter(**search_info,**data_info).count()
        data = {}
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
                
        return JsonResponse(data)        
    else:
        date=bas_title.objects.filter(**data_info)[s:e].values()
        count=bas_title.objects.filter(**data_info).count()
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
    username = request.session.get("username")
    data_info=user_info_hs(username)
  
        
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
            search_info['date']=date
        if res:
            search_info['res']=res
        if username:
            search_info['username']=username
        if name:
            search_info['name']=name
        #获取数据条数
        date=record.objects.filter(**search_info,**data_info)[s:e].values()
        data = {}
        count=record.objects.filter(**search_info,**data_info).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)        
        return JsonResponse(data) 
    else:
        date=record.objects.filter(**data_info)[s:e].values()
        data = {}
        #获取数据条数
        count=record.objects.filter(**data_info).count()
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


#问题措施--未关闭，待审核，驳回，进行中，已关闭，逾期
def pc_problem_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    username = request.session.get("username")
    data_info=user_info_hs(username)

    if(request.GET.get('date')or request.GET.get('level')or request.GET.get('shift')or request.GET.get('uloc')or request.GET.get('status')):

        level=request.GET.get('level')
        shift=request.GET.get('shift')
        uloc=request.GET.get('uloc')
        date=request.GET.get('date')
        status=request.GET.get('status')
        search_info=dict()
        
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
            search_info['date']=date
        if status:
            search_info['status']=status
        #获取数据条数
        date=problem_status.objects.filter(**search_info,**data_info,status__in=['未关闭','驳回','进行中','逾期'])[s:e].values()
        data = {}
        count=problem_status.objects.filter(**search_info,**data_info,status__in=['未关闭','驳回','进行中','逾期']).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data) 
    else:
        date=problem_status.objects.filter(**data_info,status__in=['未关闭','驳回','进行中','逾期'])[s:e].values()
        data = {}
        #获取数据条数
        count=problem_status.objects.filter(**data_info,status__in=['未关闭','驳回','进行中','逾期']).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        
        return JsonResponse(data)



#问题措施编辑
def edit_problem_api(request):    
    id=request.POST.get('id')
    pic=request.POST.get('pic')
    department=request.POST.get('department')
    method=request.POST.get('method')
    
    date=request.POST.get('date')
    reason=request.POST.get('reason')
    print(date)
    
    status=request.POST.get('status')
    if(date):
        problem_status.objects.filter(id=id).update(department=department,pic=pic,method=method,plan_close_date=date,status=status,reason=reason)
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    else:
        problem_status.objects.filter(id=id).update(department=department,pic=pic,method=method,status=status,reason=reason)
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)


#问题措施删除
def delete_problem_api(request):    
    #批量删除
    if(request.POST.get('data')):
        data=json.loads(request.POST.get('data'))
        print(data)
        for i in data:
            id=i['id']
            problem_status.objects.filter(id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)







#措施审核
def pc_confirm_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    username = request.session.get("username")
    data_info=user_info_hs(username)

    if(request.GET.get('date')or request.GET.get('level')or request.GET.get('shift')or request.GET.get('uloc')or request.GET.get('status')):

        level=request.GET.get('level')
        shift=request.GET.get('shift')
        uloc=request.GET.get('uloc')
        date=request.GET.get('date')
        status=request.GET.get('status')
        search_info=dict()
        
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
            search_info['date']=date
        if status:
            search_info['status']=status
        #获取数据条数
        date=problem_status.objects.filter(**search_info,**data_info,status__in=['进行中','待审核','逾期'])[s:e].values()
        data = {}
        count=problem_status.objects.filter(**search_info,**data_info,status__in=['进行中','待审核','逾期']).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data) 
    else:
        date=problem_status.objects.filter(**data_info,status__in=['进行中','待审核','逾期'])[s:e].values()
        data = {}
        #获取数据条数
        count=problem_status.objects.filter(**data_info,status__in=['进行中','待审核','逾期']).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        
        return JsonResponse(data)

#审核编辑
def edit_confirm_api(request):    
    id=request.POST.get('id')
    status=request.POST.get('status')
    refuse_res=request.POST.get('refuse_res')
    refuse_person=request.POST.get('refuse_person')
    if(status=='驳回'):
        datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        problem_status.objects.filter(id=id).update(status=status,refuse_res=refuse_res,refuse_person=refuse_person,refuse_time=datetime)
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)

    elif(status=='已关闭'):
        datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        problem_status.objects.filter(id=id).update(status=status,refuse_res=refuse_res,refuse_person=refuse_person,actual_close_date=datetime)
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    else:
        problem_status.objects.filter(id=id).update(status=status,refuse_res=refuse_res,refuse_person=refuse_person)
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)




#问题跟踪、问题汇总
def pc_track_api(request):
    #分页
    page=request.GET.get('page')
    limit=request.GET.get('limit')
    page=int(page)-1
    limit=int(limit)
    s=page*limit
    e=s+limit
    username = request.session.get("username")
    data_info=user_info_hs(username)
    if(request.GET.get('date')or request.GET.get('level')or request.GET.get('shift')or request.GET.get('uloc')or request.GET.get('status')):

        level=request.GET.get('level')
        shift=request.GET.get('shift')
        uloc=request.GET.get('uloc')
        date=request.GET.get('date')
        status=request.GET.get('status')
        search_info=dict()
        
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
            search_info['date']=date
        if status:
            search_info['status']=status
        #获取数据条数
        date=problem_status.objects.filter(**search_info,**data_info)[s:e].values()
        data = {}
        count=problem_status.objects.filter(**search_info,**data_info).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        return JsonResponse(data) 
    else:
        date=problem_status.objects.filter(**data_info)[s:e].values()
        data = {}
        #获取数据条数
        count=problem_status.objects.filter(**data_info).count()
        data['code']=0
        data['msg']=""
        data['count']=count
        data['data']=list(date)
        
        return JsonResponse(data)

#删除
def record_delete_api(request):
    today=datetime.date.today()
    #批量删除
    if(request.POST.get('data')):
        data=json.loads(request.POST.get('data'))
        print(data)
        for i in data:
            id=i['id']
            record.objects.filter(id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    if(request.POST.get('id')):
        id=request.POST.get('id')
        print(id)        
        record.objects.filter(id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)