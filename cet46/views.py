from django.shortcuts import render,redirect,Http404,HttpResponse
from cet46 import models
from .models import Topic,Cet_application
import xlwt
from io import StringIO
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request,'cet46/index.html')

def AdminSite(request):
    return redirect(admin.site.urls)


def topic(request):
    """显示CET 主题"""
    topic = Topic.objects.order_by('date_added')
    context1 = {'topic':topic}
    return render(request, 'cet46/CetTopic.html', context1)


def ExportData(request):
    # 设置HttpResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=user.xls'
    # new一个文件
    wb = xlwt.Workbook(encoding='utf-8')
    # new一个sheet
    sheet = wb.add_sheet(u'考生信息')
    # 维护一些样式， style_heading, style_body, style_red, style_green

    style_heading = xlwt.easyxf("""
                font:
                    name Arial,
                    colour_index white,
                    bold on,
                    height 0xA0;
                align:
                    wrap off,
                    vert center,
                    horiz center;
                pattern:
                    pattern solid,
                    fore-colour 0x19;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """
                               )

    style_body = xlwt.easyxf("""
                font:
                    name Arial,
                    bold off,
                    height 0XA0;
                align:
                    wrap on,
                    vert center,
                    horiz left;
                borders:
                    left THIN,
                    right THIN,
                    top THIN,
                    bottom THIN;
                """
                         )

    style_green = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x11;")
    style_red = xlwt.easyxf(" pattern: pattern solid,fore-colour 0x0A;")
    fmts = [
    'M/D/YY',
    'D-MMM-YY',
    'D-MMM',
    'MMM-YY',
    'h:mm AM/PM',
    'h:mm:ss AM/PM',
    'h:mm',
    'h:mm:ss',
    'M/D/YY h:mm',
    'mm:ss',
    '[h]:mm:ss',
    'mm:ss.0',
    ]

    style_body.num_format_str = fmts[0]
    # 写标题栏
    sheet.write(0, 0, '考试类型', style_heading)
    sheet.write(0, 1, '姓名', style_heading)
    sheet.write(0, 2, '身份证号', style_heading)
    sheet.write(0, 3, '性别id', style_heading)
    sheet.write(0, 4, '性别' ,style_heading)
    sheet.write(0, 5, '年龄', style_heading)
    sheet.write(0, 6, '手机号', style_heading)
    sheet.write(0, 7, '学校名称', style_heading)
    sheet.write(0, 8, '住址', style_heading)
    sheet.write(0, 9, '所有者用户', style_heading)
    # sheet.write(0, 9, '部门', style_heading)
    # sheet.write(0, 10, '人员状态',style_heading)

    # 写数据
    row = 0
    CetData = Cet_application.objects.filter(topic_id=1)
    CetDataList = {'CetData':CetData}
    print(CetData)
    for usa in CetData:
        sheet.write(row, 0, usa.topic, style_body)
        sheet.write(row, 1, usa.username, style_body)
        sheet.write(row, 2, usa.user_id, style_body)
        sheet.write(row, 3, usa.gender, style_body)

        sheet.write(row, 5, usa.age, style_body)
        sheet.write(row, 6, usa.phone, style_body)
        sheet.write(row, 7, usa.school, style_body)
        sheet.write(row, 8, usa.addr, style_body)
        sheet.write(row, 9, usa.owner, style_body)
        # sheet.write(row, 9, usa.depart, style_body)
        if int(usa.gender) == 1:
            sheet.write(row, 4, '男')
            # sheet.write(row, 10, '在职', style_green)
        else:
            sheet.write(row, 4, '女')
            # sheet.write(row, 10, '离职', style_red)
        row = row + 1

    # 写出到IO
    output = StringIO.StringIO()
    wb.save(output)
    # 重新定位到开始
    output.seek(0)
    response.write(output.getvalue())
    return response


# def UpLoadImg(request):
#     if request.method == 'POST':
#         new_img = IMG(
#             img=request.FILES.get('img'),
#             name = request.FILES.get('img').name,
#             # owner = request.FILES.get('img').owner
#             owner = request.user
#         )
#         new_img.save()
#     return render(request, 'cet46/uploadimg.html')


# def Cetapply(request,topic_id):
#     topic = Topic.objects.get(id=topic_id)
#
#     if request.method != 'POST':
#         form = CetForm
#     else:
#         form = CetForm(data=request.POST)
#         if form.is_valid():
#             new_cet = form.save(commit=False)
#             new_cet.topic = topic
#             new_cet.save()
#             return HttpResponseRedirect(reverse('cet46:index',args=[topic_id]))
#
#     context = {'topic':topic,'form':form}
#     return render(request,'cet46/cetForm.html',context)

@login_required
# def Apply(request,topi_id):
#     CurrentCetList = Cet_application.objects.filter(owner=request.user)
#     context = {'topi_id':topi_id}
#     return render(request,'cet46/Apply.html',context)
# topic = Topic.objects.get(id=topic_id)
@login_required
def personal_info(request):
    CurrentCetList = Cet_application.objects.filter(owner=request.user)
    print(CurrentCetList)
    return render(request, 'cet46/perInfo.html', {'CurrentCetList': CurrentCetList})
    # ImgList = IMG.objects.get(owner=request.user)
    # idd = ImgList.id
    # img = ImgList.img
    #
    # print(ImgList)
    # print(idd)
    # print(img)

    # for row in CurrentCetList:
    #     print(row.user_id)
    # perInfo = Cet_application.objects.get(topic_id=1)
    # perTopic_id = perInfo.topic_id
    # perName = perInfo.username
    # perUser_id = perInfo.user_id
    # perGender = perInfo.gender
    # perAge = perInfo.age
    # perPhone = perInfo.phone
    # perSchool = perInfo.school
    # perAddr = perInfo.addr
    # print(perAddr)

    # context = {'username': perName, 'user_id': perUser_id, 'gender': perGender, 'age': perAge, 'phone': perPhone,
    #            'school': perSchool, 'addr': perAddr}
    # if (IMG.objects.filter(owner=request.user)):
    # return render(request, 'cet46/perInfo.html', {'CurrentCetList': CurrentCetList, 'img_id': idd,'img':img})
    # CurrentCetList = Cet_application.objects.filter(owner=request.user)



@login_required
def CetForms(request,topi_id):
    if (Cet_application.objects.filter(owner=request.user)):
        #perInfo = Cet_application.objects.get(topic_id=topi_id)
        # perTopic_id = perInfo.topic_id
        # perName = perInfo.username
        # perUser_id = perInfo.user_id
        # perGender = perInfo.gender
        # perAge = perInfo.age
        # perPhone = perInfo.phone
        # perSchool = perInfo.school
        # perAddr = perInfo.addr
        # print(perAddr)

        #perInfoList = Cet_application.objects.filter(owner=request.user)
        # context = {'username': perName, 'user_id': perUser_id, 'gender': perGender, 'age': perAge, 'phone': perPhone,
        #            'school': perSchool, 'addr': perAddr}
        return render(request, 'cet46/AlreadyApply.html')

    else:
        if request.method == 'GET':
            cet_list = models.Topic.objects.all()
            context = {'topi_id': topi_id}
            return render(request, 'cet46/CetForm.html', context)
        elif request.method == 'POST' and request.method == True:
                username = request.POST.get('username', '')
                user_id = request.POST.get('user_id', '')
                gender = request.POST.get('gender', '')
                age = request.POST.get('age', '')
                phone = request.POST.get('phone', '')
                school = request.POST.get('school', '')
                addr = request.POST.get('addr', '')
                img = request.FILES.get('img')
                owner = request.user
                models.Cet_application.objects.create(

                    username=username,
                    user_id=user_id,
                    gender=gender,
                    age=age,
                    phone=phone,
                    school=school,
                    addr=addr,
                    topic_id=topi_id,
                    owner=owner
                )
                return redirect('cet46:index')


def edit_cetForm(request,row_id):
    if request.method=="GET":
        #nid = request.GET.get('nid', '')
        obj=models.Cet_application.objects.get(id=row_id)
        print(row_id)
        print(obj)
        context = {'obj':obj}
        # cet_id = obj.id
        # username = obj.username
        # user_id = obj.user_id
        # gender = obj.gender
        # age = obj.age
        # phone = obj.phone
        # school = obj.school
        # addr = obj.addr
        # content1 = {'cet_id':cet_id,'username':username,'user_id':user_id,'gender':gender,'age':age,
        #             'phone':phone,'school':school,'addr':addr}
        #cs_list = models.Classes.objects.all()
        return render(request, 'cet46/Edit_info.html', context)

    elif request.method=='POST':
        username = request.POST.get('username', '')
        user_id = request.POST.get('user_id', '')
        gender = request.POST.get('gender', '')
        age = request.POST.get('age','')
        phone = request.POST.get('phone', '')
        school = request.POST.get('school','')
        addr = request.POST.get('addr','')
        models.Cet_application.objects.filter(id=row_id).update(

            username=username,
            user_id = user_id,
            gender=gender,
            age=age,
            phone = phone,
            school = school,
            addr = addr)
        return redirect('cet46:index')