# Generated by Django 2.2.1 on 2020-01-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_problem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bas_title',
            name='title_fl',
            field=models.CharField(max_length=20, null=True, verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='bas_title',
            name='title_lb',
            field=models.CharField(max_length=20, null=True, verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='bas_title',
            name='title_wd',
            field=models.CharField(max_length=20, null=True, verbose_name='维度'),
        ),
        migrations.AddField(
            model_name='plan_status',
            name='title_fl',
            field=models.CharField(max_length=20, null=True, verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='plan_status',
            name='title_lb',
            field=models.CharField(max_length=20, null=True, verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='plan_status',
            name='title_wd',
            field=models.CharField(max_length=20, null=True, verbose_name='维度'),
        ),
        migrations.AddField(
            model_name='problem_status',
            name='title_fl',
            field=models.CharField(max_length=20, null=True, verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='problem_status',
            name='title_lb',
            field=models.CharField(max_length=20, null=True, verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='problem_status',
            name='title_wd',
            field=models.CharField(max_length=20, null=True, verbose_name='维度'),
        ),
        migrations.AddField(
            model_name='record',
            name='title_fl',
            field=models.CharField(max_length=20, null=True, verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='record',
            name='title_lb',
            field=models.CharField(max_length=20, null=True, verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='record',
            name='title_wd',
            field=models.CharField(max_length=20, null=True, verbose_name='维度'),
        ),
        migrations.AlterField(
            model_name='problem_status',
            name='reason',
            field=models.CharField(max_length=100, null=True, verbose_name='原因'),
        ),
        migrations.AlterField(
            model_name='record',
            name='name',
            field=models.CharField(max_length=10, null=True, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='record',
            name='reason',
            field=models.CharField(max_length=100, null=True, verbose_name='原因'),
        ),
    ]