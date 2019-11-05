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
    for i in range(row):
        item_info['workshop']=df.iloc[i,0]
        item_info['worksection']=df.iloc[i,1]
        item_info['team']=df.iloc[i,2]       
        item_info['level']=df.iloc[i,3]       
        item_info['shift']=df.iloc[i,4]       
        item_info['uloc']=df.iloc[i,5]       
        item_info['date']=df.iloc[i,6]       
        item_info['title']=df.iloc[i,7]              
        bas_title.objects.create(**item_info)
        item_info=dict()

    data = {}
    data['code']=0
    data['msg']=""
    data['data']='ok'
    return JsonResponse(data)


#模板下载
def item_templates_download(request):
    file=open('D:/plant/templates/items.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="items.xlsx"'
    return response


#删除
def item_delete_api(request):
    #批量删除
    if(request.POST.get('data')):
        data=json.loads(request.POST.get('data'))
        print(data)
        for i in data:
            id=i['id']
            bas_title.objects.filter(id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    if(request.POST.get('id')):
        id=request.POST.get('id')
        print(id)
        bas_title.objects.filter(id=id).delete()
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)

#新增或者更新
def edit_item_api(request):
    id=request.POST.get('id')
    if id:
        update_info=dict()    
        update_info['workshop']=request.POST.get('workshop')
        update_info['worksection']=request.POST.get('worksection')
        update_info['team']=request.POST.get('team')
        update_info['level']=request.POST.get('level')
        update_info['shift']=request.POST.get('shift')
        update_info['uloc']=request.POST.get('uloc')
        update_info['date']=request.POST.get('date')
        update_info['title']=request.POST.get('title')

        bas_title.objects.filter(id=id).update(**update_info)
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)
    else:
        add_info=dict()    
        add_info['workshop']=request.POST.get('workshop')
        add_info['worksection']=request.POST.get('worksection')
        add_info['team']=request.POST.get('team')
        add_info['level']=request.POST.get('level')
        add_info['shift']=request.POST.get('shift')
        add_info['uloc']=request.POST.get('uloc')
        add_info['date']=request.POST.get('date')
        add_info['title']=request.POST.get('title')

        bas_title.objects.create(**add_info)
        res = {}
        res['res'] = 'ok'
        return JsonResponse(res)       