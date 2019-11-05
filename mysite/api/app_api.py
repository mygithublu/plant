from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from mysite.models import zzuser,bas_title,record
import datetime
import json






#获取点检内容
def get_title_api(request):
    username=request.POST.get('username')

    uloc=request.POST.get('uloc')
    level=request.POST.get('level')
    shift=request.POST.get('shift')

    #取消原通过用户名关联的工位，修改为前端选择
    # uloc=zzuser.objects.all().values().filter(username=username)[0]['uloc']

    today=datetime.date.today()
    title={}
    data=bas_title.objects.filter(uloc=uloc,level=level,date=today,status='0',shift=shift).values()
    title['title']=list(data)
    return JsonResponse(title)



#点检提交API
def submit_api(request):
    id=request.POST.get('id')
    check=request.POST.get('checkvalue')
    res=''
    reason=request.POST.get('reason')
    username=request.POST.get('username')
    today=datetime.date.today()
    title_info=bas_title.objects.filter(id=id).values()
    workshop=title_info[0]['workshop']
    worksection=title_info[0]['worksection']
    team=title_info[0]['team']
    level=title_info[0]['level']
    shift=title_info[0]['shift']
    uloc=title_info[0]['uloc']
    date=title_info[0]['date']
    title=title_info[0]['title']
    if(check=='1'):
        res='OK'
    elif(check=='0'):
        res='NOK'
    else:
        res='NA'
    if(check=='0'):
        reason=reason
    else:
        reason=''
    res_time=datetime.date.today()
    name=zzuser.objects.filter(username=username).values()
    name=name[0]['name']
    record.objects.create(workshop=workshop,worksection=worksection,team=team,level=level,shift=shift,date=date,title=title,res=res,reason=reason,res_time=res_time,username=username,name=name,uloc=uloc)
    
    bas_title.objects.filter(id=id).update(status='1')
    
    result={}
    result['ok']='ok'
    return JsonResponse(result) 


#用户登录api
def login_api(request):
    # zzuser.objects.create(username='test01',password='123456',psn='Z001',name='小明',workshop='GA1',worksection='1T1',team='T1',shift='A',level='班组长',uloc='T1001')
    # zzuser.objects.create(username='test02',password='123456',psn='Z001',name='小明',workshop='GA1',worksection='1T1',team='T1',shift='A',level='班组长',uloc='T1001')

    # bas_title.objects.create(workshop='GA1',worksection='1T1',team='T1',level='班组长',shift='A',uloc='T1001L',date='2019-09-12',title='操作是否符合作业指导书（SOS/JIS/MDS）的要求?')
    # bas_title.objects.create(workshop='GA1',worksection='1T1',team='T1',level='班组长',shift='A',uloc='T1001L',date='2019-09-12',title='操作是否符合作业指导书（SOS/JIS/MDS）的要求?')


    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username)
    ok=zzuser.objects.filter(username=username,password=password)
    if(ok):
        res={}
        res['res']=1
        res['username']=username
        return JsonResponse(res)
    else:
        res={}
        res['res']=0
        return JsonResponse(res)        


    res={}
    res['res']=1
    return JsonResponse(res)