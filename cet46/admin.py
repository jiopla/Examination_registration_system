from django.contrib import admin
from cet46.models import Topic
from cet46.models import Cet_application
from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = '英语考试报名管理系统'  # 此处设置页面显示标题
    site_title = '英语考试'  # 此处设置页面头部标题


admin_site = MyAdminSite(name='management')


class TitleList(admin.ModelAdmin):
    actions = ["SaveExecl", ]
    list_display = ('topic','username','user_id','gender','age','phone','school','addr','owner')
    search_fields = ('topic','username','user_id','gender','age','phone','school','addr','owner')

class TopicTitle(admin.ModelAdmin):
    list_display = ('id','text')

# Register your models here.
admin.site.register(Cet_application,TitleList)
admin.site.register(Topic,TopicTitle)

admin.site.site_header = '在线英语考试系统后台'
admin.site.site_title = '在线英语考试报名系统'



