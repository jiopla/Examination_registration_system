from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.contrib import admin
from django.shortcuts import render,redirect
from django.conf.urls import url
from django.urls import path
from django.conf import settings  # 这一行需要引入
from django.conf.urls.static import static  # 这一行需要引入

from . import views

app_name='cet46'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/',views.AdminSite,name='AdminSite'),
    url(r'^CetTopic/$',views.topic,name='topic'),
    url(r'^CetPersInfo/$',views.personal_info,name='personal_info'),
    url(r'^cetForms/(?P<topi_id>\d+)/$',views.CetForms,name='CetForms'),
    # url(r'^ApplyCET/(?P<topi_id>\d+)/$',views.Apply,name='Apply'),
    url(r'^EditInfo/(?P<row_id>\d+)/$',views.edit_cetForm,name='edit_cetForm'),
    url(r'^ExportData/$',views.ExportData,name='ExportData')
    # url(r'^upLoad/$',views.UpLoadImg,name='UpLoadImg')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 加上statis
# urlpatterns += staticfiles_urlpatterns()