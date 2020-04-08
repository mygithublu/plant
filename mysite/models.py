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
    title=models.CharField('检查项',null=False,max_length=300)
    status=models.CharField('检查状态',null=False,default='0',max_length=5)
    createtime=models.DateTimeField('创建时间',auto_now_add=True)
    updatetime=models.DateTimeField('更新时间',auto_now=True)
    #20200117新增类别、维度、分类字段
    title_lb=models.CharField('类别',null=True,max_length=20)
    title_wd=models.CharField('维度',null=True,max_length=20)
    title_fl=models.CharField('分类',null=True,max_length=20)

    class Meta:
        ordering=['id']



#点检计划
class pc_plan(models.Model):
    workshop=models.CharField('车间',null=False,max_length=10)
    worksection=models.CharField('工段',null=False,max_length=10)
    team=models.CharField('班组',null=False,max_length=10)
    level=models.CharField('层级',null=False,max_length=10)
    shift=models.CharField('班次',null=False,max_length=5)
    uloc=models.CharField('工位',null=False,max_length=20)
    date=models.DateField('日期',null=False)
    status=models.CharField('检查状态',null=False,default='0',max_length=5)
    createtime=models.DateTimeField('创建时间',auto_now_add=True)
    updatetime=models.DateTimeField('更新时间',auto_now=True)
    class Meta:
        ordering=['id']


# # 点检计划状态
class plan_status(models.Model):
    item_id=models.CharField('点检项目id',null=False,max_length=20)
    plan_id=models.CharField('点检计划id',null=False,max_length=20)
    workshop=models.CharField('车间',null=False,max_length=10)
    worksection=models.CharField('工段',null=False,max_length=10)
    team=models.CharField('班组',null=False,max_length=10)
    level=models.CharField('层级',null=False,max_length=10)
    shift=models.CharField('班次',null=False,max_length=5)
    uloc=models.CharField('工位',null=False,max_length=20)
    title=models.CharField('检查项',null=False,max_length=300)    
    date=models.DateField('日期',null=False)
    status=models.CharField('检查状态',null=False,default='0',max_length=5)
    createtime=models.DateTimeField('创建时间',auto_now_add=True)
    updatetime=models.DateTimeField('更新时间',auto_now=True)
    
    #20200117新增类别、维度、分类字段
    title_lb=models.CharField('类别',null=True,max_length=20)
    title_wd=models.CharField('维度',null=True,max_length=20)
    title_fl=models.CharField('分类',null=True,max_length=20)


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
    reason=models.CharField('原因',null=True,max_length=100)
    res_time=models.DateField('检查日期',null=False)
    username=models.CharField('用户名',null=False,max_length=20)
    name=models.CharField('名字',null=True,max_length=10)
    createtime=models.DateTimeField('创建时间',auto_now_add=True)
    #20200117新增类别、维度、分类字段
    title_lb=models.CharField('类别',null=True,max_length=20)
    title_wd=models.CharField('维度',null=True,max_length=20)
    title_fl=models.CharField('分类',null=True,max_length=20)


    class Meta:
        ordering=['id']

class app_vesion(models.Model):
    appvesion=models.CharField('版本号',null=False,max_length=20)
    class Meta:
        ordering=['id']


# 问题状态表--未关闭，待审核，驳回，进行中，已关闭，逾期
class problem_status(models.Model):
    workshop=models.CharField('车间',null=False,max_length=10)
    worksection=models.CharField('工段',null=False,max_length=10)
    team=models.CharField('班组',null=False,max_length=10)
    level=models.CharField('层级',null=False,max_length=10)
    shift=models.CharField('班次',null=False,max_length=5)
    uloc=models.CharField('工位',null=False,max_length=20)
    date=models.DateField('计划日期',null=False)
    title=models.CharField('检查项',null=False,max_length=300)
    res=models.CharField('检查结果',null=False,max_length=5)
    reason=models.CharField('原因',null=True,max_length=100)
    createtime=models.DateTimeField('检查时间',auto_now_add=True)
    username=models.CharField('用户名',null=False,max_length=20)
    name=models.CharField('名字',null=False,max_length=10)
    department=models.CharField('责任部门',null=True,max_length=20)
    pic=models.CharField('责任人',null=True,max_length=20)
    method=models.CharField('问题措施',null=True,max_length=300)
    plan_close_date=models.DateField('计划关闭日期',null=True)
    status=models.CharField('问题状态',null=False,max_length=10)
    actual_close_date=models.DateTimeField('实际关闭日期',null=True)
    refuse_person=models.CharField('驳回人',null=False,max_length=10)
    refuse_res=models.CharField('驳回原因',null=True,max_length=300)
    refuse_time=models.DateTimeField('驳回时间',null=True)
    updatetime=models.DateTimeField('创建时间',auto_now_add=True)


    #20200117新增类别、维度、分类字段
    title_lb=models.CharField('类别',null=True,max_length=20)
    title_wd=models.CharField('维度',null=True,max_length=20)
    title_fl=models.CharField('分类',null=True,max_length=20)

    class Meta:
        ordering=['id']