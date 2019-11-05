# Generated by Django 2.2 on 2019-09-12 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zzuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('psn', models.CharField(max_length=20, verbose_name='工号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('workshop', models.CharField(max_length=20, verbose_name='车间')),
                ('worksection', models.CharField(max_length=20, verbose_name='工段')),
                ('team', models.CharField(max_length=20, verbose_name='班组')),
                ('shift', models.CharField(max_length=2, verbose_name='班次')),
                ('level', models.CharField(max_length=10, verbose_name='层级')),
                ('uloc', models.CharField(max_length=20, verbose_name='工位')),
                ('createtime', models.DateField(auto_now_add=True, verbose_name='创建日期')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]