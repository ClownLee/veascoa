# from django.shortcuts import render
import re, json
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from . import models

# Create your views here.
class Admins(View):

    @require_http_methods(['POST'])
    def addAdmin(request):
        # print(request.GET.get('id', default=None))
        try:
            req = json.loads(request.body.decode('utf-8'))

            username = req.get('username')
            if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]{5,11}$', username) == None:
                raise Exception('用户名6-12个字符且必须以字母或下划线开头')

            phone = req.get('phone')
            if re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', phone) == None:
                raise Exception('手机号码输入错误')

            email = req.get('email')
            if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)$', email) == None:
                raise Exception('邮箱输入错误')

            password = req.get('password')
            if re.match(r"^(?![A-Za-z0-9]+$)(?![a-z0-9\\W]+$)(?![A-Za-z\\W]+$)(?![A-Z0-9\\W]+$)^.{8,}$", password) == None:
                raise Exception('密码至少8位含大小写字母、数字、特殊符号的字符')

            avator = req.get('avator')
            if avator != None and len(avator) > 0 and re.match(r'^http(s)?:\/\/([\w.]+\/?)\S*', avator) == None:
                raise Exception('头像地址错误')

            admins = models.Admins(username=username, phone=phone, email=email, password=password, avator=avator)
            admins.save()
            return JsonResponse({ "code": 0, "data": [], "message": "操作成功" })
        except Exception as e:
            return JsonResponse({ "code": 1, "data": [], "message": str(e) })
    
    @require_http_methods(['POST'])
    def updateAdmin(request):
        try:
            req = json.loads(request.body.decode('utf-8'))
            id = req.get('id')
            if id == None or not isinstance(id, int):
                raise Exception('id不存在')
            admin = models.Admins.objects.get(id=id)

            username = req.get('username')
            if username != None:
                if len(username) > 0 and re.match(r'^[a-zA-Z_][a-zA-Z0-9_]{5,11}$', username) != None:
                    admin.username = username
                else:
                    raise Exception('用户名6-12个字符且必须以字母或下划线开头')

            is_del = req.get('is_del')
            if is_del != None:
                if int(is_del) == 0 or int(is_del) == 1:
                    user.is_del = is_del
                else:
                    raise Exception('删除/启用账号失败')

            phone = req.get('phone')
            if phone != None:
                if len(phone) > 0 and re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', phone) != None:
                    admin.phone = phone
                else:
                    raise Exception('手机号码输入错误')

            email = req.get('email')
            if email != None:
                if len(email) > 0 and re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)$', email) != None:
                    admin.email = email
                else:
                    raise Exception('邮箱输入错误')

            password = req.get('password')
            if password != None:
                if len(password) > 0 and re.match(r"^(?![A-Za-z0-9]+$)(?![a-z0-9\\W]+$)(?![A-Za-z\\W]+$)(?![A-Z0-9\\W]+$)^.{8,}$", password) != None:
                    admin.password = password
                else:
                    raise Exception('密码至少8位含大小写字母、数字、特殊符号的字符')

            avator = req.get('avator')
            if avator != None:
                if len(avator) != 0 and re.match(r'^http(s)?:\/\/([\w.]+\/?)\S*', avator) != None:
                    admin.avator = avator
                else:
                    raise Exception('头像地址错误')
            
            admin.save()
            return JsonResponse({ 'code': 0, 'data': [], 'message': '操作成功' })
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], 'message': str(e) })

    def getAdminOne(id):
        res = models.Admins.objects.get(id=id)
        return res.toJson()


    def getAdminsList(page, size):

        res = models.Admins.objects.all()[(page - 1) * size : page * size]
        json = []
        for i in res:
            json.append(i.toJson())

        total = models.Admins.objects.count()
        return {
            'page': page,
            'size': size,
            'total': total,
            'list': json
        }

    
    @require_http_methods(['GET'])
    def getAdmins(request):
        req = json.loads(request.body.decode('utf-8'))
        id = req.get('id')
        if id != None and isinstance(id, int) and id > 0:
            print('okokook')
            res = Admins.getAdminOne(id=id)
        else:
            page = req.get('page')
            size = req.get('size')
            res = Admins.getAdminsList(page=page, size=size)

        return JsonResponse({ 'code': 0, 'data': res, 'message': '操作成功' })