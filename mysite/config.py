from mysite.models import zzuser


# 导航等初始化
init_config = {
    "clearInfo": {
        "clearUrl": "api/clear.json"
    },
    "homeInfo": {
        "title": "首页",
        "icon": "fa fa-home",
        "href": "welcome/"
    },
    "logoInfo": {
        "title": "郑班组",
        "image": "images/logo.png",
        "href": ""
    },
    "menuInfo": {
        "currency": {
            "title": "常规管理",
            "icon": "fa fa-address-book",
            "child": [{
                    "title": "系统配置",
                    "href": "",
                    "icon": "fa fa-home",
                    "target": "_self",
                    "child": [{
                            "title": "系统账号",
                            "href": "user/",
                            "icon": "fa fa-child",
                            "target": "_self"
                    },
                        #     {
                        #         "title": "系统菜单",
                        #         "href": "menu/",
                        #         "icon": "fa fa-tachometer",
                        #         "target": "_self"
                        # }
                    ]
            },
                {
                "title": "分层审核",
                    "href": "",
                    "icon": "fa fa-window-maximize",
                    "target": "_self",
                    "child": [{
                            "title": "点检项目",
                            "href": "items/",
                            "icon": "fa fa-list-alt",
                            "target": "_self"
                    },
                        {
                            "title": "制定计划",
                            "href": "pc_plan/",
                            "icon": "fa fa-gears",
                            "target": "_self"
                    },
                        {
                            "title": "点检记录",
                            "href": "record/",
                            "icon": "fa fa-area-chart",
                            "target": "_self"
                    },
                        {
                            "title": "问题措施",
                            "href": "problem/",
                            "icon": "fa fa-building",
                            "target": "_self"
                    },
                        {
                            "title": "措施审核",
                            "href": "confirm/",
                            "icon": "fa fa-book",
                            "target": "_self"
                    },
                        {
                            "title": "问题汇总",
                            "href": "track/",
                            "icon": "fa fa-bar-chart",
                            "target": "_self"
                    }

                    ]
            },

                {
                    "title": "监控报警",
                    "href": "layout/",
                    "icon": "fa fa-bell",
                    "target": "_blank"
            },                              
              
            ]
        },
        # "component": {
        #     "title": "组件管理",
        #     "icon": "fa fa-lemon-o",
        #     "child": [{
        #             "title": "图标列表",
        #             "href": "page/icon.html",
        #             "icon": "fa fa-dot-circle-o",
        #             "target": "_self"
        #     },
        #         {
        #             "title": "图标选择",
        #             "href": "page/icon-picker.html",
        #             "icon": "fa fa-adn",
        #             "target": "_self"
        #     },
        #         {
        #             "title": "颜色选择",
        #             "href": "page/color-select.html",
        #             "icon": "fa fa-dashboard",
        #             "target": "_self"
        #     },
        #         {
        #             "title": "下拉选择",
        #             "href": "page/table-select.html",
        #             "icon": "fa fa-angle-double-down",
        #             "target": "_self"
        #     },
        #         {
        #             "title": "文件上传",
        #             "href": "page/upload.html",
        #             "icon": "fa fa-arrow-up",
        #             "target": "_self"
        #     },
        #         {
        #             "title": "富文本编辑器",
        #             "href": "page/editor.html",
        #             "icon": "fa fa-edit",
        #             "target": "_self"
        #     }
        #     ]
        # },
        # "other": {
        #     "title": "其它管理",
        #     "icon": "fa fa-slideshare",
        #     "child": [{
        #             "title": "多级菜单",
        #             "href": "",
        #             "icon": "fa fa-meetup",
        #             "target": "",
        #             "child": [{
        #                 "title": "按钮1",
        #                 "href": "page/button.html",
        #                 "icon": "fa fa-calendar",
        #                 "target": "_self",
        #                 "child": [{
        #                     "title": "按钮2",
        #                     "href": "page/button.html",
        #                     "icon": "fa fa-snowflake-o",
        #                     "target": "_self",
        #                     "child": [{
        #                             "title": "按钮3",
        #                             "href": "page/button.html",
        #                             "icon": "fa fa-snowflake-o",
        #                             "target": "_self"
        #                     },
        #                         {
        #                             "title": "表单4",
        #                             "href": "page/form.html",
        #                             "icon": "fa fa-calendar",
        #                             "target": "_self"
        #                     }
        #                     ]
        #                 }]
        #             }]
        #     },
        #         {
        #             "title": "失效菜单",
        #             "href": "page/error.html",
        #             "icon": "fa fa-superpowers",
        #             "target": "_self"
        #     }
        #     ]
        # }
    }
}


#获取用户的车间工段班组信息
def user_info_hs(username):        
    user_info=zzuser.objects.filter(username=username).values()
    workshop=user_info[0]['workshop']
    worksection=user_info[0]['worksection']
    team=user_info[0]['team']
    level=''
    if (user_info[0]['level']=='班组长'):
        level=user_info[0]['level']
    shift=user_info[0]['shift']

    data_info={}
    if workshop:
        data_info['workshop']=workshop
    if worksection:
        data_info['worksection']=worksection
    if team:
        data_info['team']=team
    if level:
        data_info['level']=level
    if shift:
        data_info['shift']=shift
    return data_info