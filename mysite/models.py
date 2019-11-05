from django.db import models

# Create your models here.
#用户
class zzuser(models.Model):
    username=models.CharField('用户名',null=False,unique=True,max_length=20)
    password=models.CharField('密码',null=False,max_length=20)
    psn=models.CharField('工号',null=False,max_length=20)
    name=models.CharField('姓名',null=False,max_length=20)
    workshop=models.CharField('车间',null=False,max_length=20)
    worksection=models.CharField('工段',null=False,max_length=20)
    team=models.CharField('班组',null=False,max_length=20)
    shift=models.CharField('班次',null=False,max_length=2)
    level=models.CharField('层级',null=False,max_length=10)
    uloc=models.CharField('工位',null=False,max_length=20)
    is_admin=models.CharField('是否管理员',null=True,max_length=5)
    createtime=models.DateField('创建日期',null=False,auto_now_add=True)
    class Meta:
        ordering = ['id']

#检查主数据
class bas_title(models.Model):
    workshop=models.CharField('车间',null=False,max_length=10)
    worksection=models.CharField('工段',null=False,max_length=10)
    team=models.CharField('班组',null=False,max_length=10)
    level=models.CharField('层级',null=False,max_length=10)
    shift=models.CharField('班次',null=False,max_length=5)
    uloc=models.CharField('工位',null=False,max_length=20)
    date=models.DateField('日期',null=False)
    title=models.CharField('检查项',null=False,max_length=300)
    status=models.CharField('检查状态',null=False,default='0',max_length=5)
    createtime=models.DateTimeField('创建时间',auto_now_add=True)
    updatetime=models.DateTimeField('更新时间',auto_now=True)
    class Meta:
        ordering=['id']



class record(models.Model):
    workshop=models.CharField('车间',null=False,max_length=10)
    worksection=models.CharField('工段',null=False,max_length=10)
    team=models.CharField('班组',null=False,max_length=10)
    level=models.CharField('层级',null=False,max_length=10)
    shift=models.CharField('班次',null=False,max_length=5)
    uloc=models.CharField('工位',null=False,max_length=20)
    date=models.DateField('日期',null=False)
    title=models.CharField('检查项',null=False,max_length=300)
    res=models.CharField('检查结果',null=False,max_length=5)
    reason=models.CharField('原因',null=False,max_length=100)
    res_time=models.DateField('检查日期',null=False)
    username=models.CharField('用户名',null=False,max_length=20)
    name=models.CharField('名字',null=False,max_length=10)
    createtime=models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        ordering=['id']

class app_vesion(models.Model):
    appvesion=models.CharField('版本号',null=False,max_length=20)
    class Meta:
        ordering=['id']