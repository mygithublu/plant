郑班组
20191108 
layout 底盘四5个班组
点检项和点检计划分开

20191120
layout 新增日期和班次选择
app获取点检项目跨天时，0-8点，日期减1天

20191130
引入layuimini 使用iframe框架
新增问题管理模块

20200116
1、问题措施界面的nook原因，修改为可以编辑，涉及内容：
problem.html
pc_api.py(edit_problem_api) 接口
2、数据权限
如果是班组长：
车间+工段+班组 修改为：车间+工段+班组+层级+班次
如果是工段长：
车间+工段+班组 修改为：车间+工段+班组+班次

涉及：
1、config.py (user_info_hs)
 level=''
    if (user_info[0]['level']=='班组长'):
        level=user_info[0]['level']
    shift=user_info[0]['shift']
if level:
    data_info['level']=level
if shift:
    data_info['shift']=shift

2、pc_api.py(items_pc_api)

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

3、plan.py(pc_plan_api)

4、pc_api.py(record_api、、pc_track_api、、pc_confirm_api、、pc_problem_api)

3:手机端登陆不需要重新选择层级和班次，按照维护的账号信息自动关联
涉及
app_api.py（login_api、get_title_api，新增get_plan_status_api）urls.py

4:新增类别、维度、分类字段
涉及：models.py、导入模板、items.html\plan.py\记录、措施、问题