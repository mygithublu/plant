# Generated by Django 2.2 on 2020-01-17 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0018_auto_20200117_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bas_title',
            old_name='title_fs',
            new_name='title_fl',
        ),
        migrations.RenameField(
            model_name='plan_status',
            old_name='title_fs',
            new_name='title_fl',
        ),
        migrations.RenameField(
            model_name='problem_status',
            old_name='title_fs',
            new_name='title_fl',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='title_fs',
            new_name='title_fl',
        ),
    ]
