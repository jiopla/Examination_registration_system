from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200,verbose_name=u'考试类型')
    date_added = models.DateTimeField(auto_now_add=True,verbose_name=u'添加时间')
    def __str__(self):
        return u'%s' %(self.text)

    class Meta:
        verbose_name = "考试类型"
        verbose_name_plural = "考试类型"




class Cet_application(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,verbose_name=u'考试类型')
    username=models.CharField(max_length=32,verbose_name=u'姓名')
    user_id = models.CharField(max_length=18,verbose_name=u'身份证号')
    gender = models.BooleanField(verbose_name=u'性别')
    age = models.CharField(max_length=8,verbose_name=u'年龄')
    phone = models.CharField(max_length=11,verbose_name=u'手机号')
    school = models.CharField(max_length=60,verbose_name=u'学校名称')
    addr = models.CharField(max_length=60,verbose_name=u'住址')
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name=u'所有者用户')

    def __str__(self):
        return u'%s %s %s %s %s %s %s %s %s' %(self.topic,self.username,self.user_id,self.gender,self.age,self.phone,self.school,self.addr,self.owner)
        # username= self.username
        # user_id = self.user_id
        # owner = self.owner
        # listtp = (username,user_id,owner)
        # list = str(listtp)
        # return list

    class Meta:
        verbose_name = "考生信息表"
        verbose_name_plural = "考生信息表"




# class Article(models.Model):
#     username = models.CharField('姓名', max_length=256)
#     user_id = models.CharField('身份证号',max_length=18)
#     owner = models.ForeignKey(User,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.username,self.user_id,self.owner