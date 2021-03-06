# Generated by Django 2.2.1 on 2019-12-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_plan_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='problem_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop', models.CharField(max_length=10, verbose_name='车间')),
                ('worksection', models.CharField(max_length=10, verbose_name='工段')),
                ('team', models.CharField(max_length=10, verbose_name='班组')),
                ('level', models.CharField(max_length=10, verbose_name='层级')),
                ('shift', models.CharField(max_length=5, verbose_name='班次')),
                ('uloc', models.CharField(max_length=20, verbose_name='工位')),
                ('date', models.DateField(verbose_name='计划日期')),
                ('title', models.CharField(max_length=300, verbose_name='检查项')),
                ('res', models.CharField(max_length=5, verbose_name='检查结果')),
                ('reason', models.CharField(max_length=100, verbose_name='原因')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='检查时间')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('name', models.CharField(max_length=10, verbose_name='名字')),
                ('department', models.CharField(max_length=20, null=True, verbose_name='责任部门')),
                ('pic', models.CharField(max_length=20, null=True, verbose_name='责任人')),
                ('method', models.CharField(max_length=300, null=True, verbose_name='问题措施')),
                ('plan_close_date', models.DateField(null=True, verbose_name='计划关闭日期')),
                ('status', models.CharField(max_length=10, verbose_name='问题状态')),
                ('actual_close_date', models.DateTimeField(null=True, verbose_name='实际关闭日期')),
                ('refuse_person', models.CharField(max_length=10, verbose_name='驳回人')),
                ('refuse_res', models.CharField(max_length=300, null=True, verbose_name='驳回原因')),
                ('refuse_time', models.DateTimeField(null=True, verbose_name='驳回时间')),
                ('updatetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
