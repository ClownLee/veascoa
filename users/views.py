# from django.shortcuts import render
import re, json
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from . import models
from django.db.models import Q
from utils.constants.index import IS_DEL

# Create your views here.
class Users(View):

    @require_http_methods(['POST'])
    def addUser(request):
        # print(request.GET.get('id', default=None))
        try:
            req = json.loads(request.body.decode('utf-8'))

            username = req.get('username')
            if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]{5,11}$', str(username)) == None:
                raise Exception('用户名6-12个字符且必须以字母或下划线开头')

            phone = req.get('phone')
            if re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', str(phone)) == None:
                raise Exception('手机号码输入错误')

            email = req.get('email')
            if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)$', str(email)) == None:
                raise Exception('邮箱输入错误')

            password = req.get('password')
            if re.match(r"^(?![A-Za-z0-9]+$)(?![a-z0-9\\W]+$)(?![A-Za-z\\W]+$)(?![A-Z0-9\\W]+$)^.{8,}$", str(password)) == None:
                raise Exception('密码至少8位含大小写字母、数字、特殊符号的字符')

            avator = req.get('avator')
            if avator != None and len(avator) > 0 and re.match(r'^http(s)?:\/\/([\w.]+\/?)\S*', str(avator)) == None:
                raise Exception('头像地址错误')

            users = models.Users(username=username, phone=phone, email=email, password=password, avator=avator)
            users.save()
            return JsonResponse({ "code": 0, "data": [], "message": "操作成功" })
        except Exception as e:
            return JsonResponse({ "code": 1, "data": [], "message": str(e) })
    
    @require_http_methods(['POST'])
    def updateUser(request):
        try:
            req = json.loads(request.body.decode('utf-8'))
            id = req.get('id')
            if id == None or not isinstance(id, int):
                raise Exception('id不存在')
            user = models.Users.objects.get(id=id)

            username = req.get('username')
            if username != None:
                if len(username) > 0 and re.match(r'^[a-zA-Z_][a-zA-Z0-9_]{5,11}$', username) != None:
                    user.username = username
                else:
                    raise Exception('用户名6-12个字符且必须以字母或下划线开头')

            is_del = req.get('is_del')
            if is_del != None:
                if int(is_del) in IS_DEL.keys():
                    user.is_del = is_del
                else:
                    raise Exception('删除/启用账号失败')

            phone = req.get('phone')
            if phone != None:
                if len(phone) > 0 and re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', phone) != None:
                    user.phone = phone
                else:
                    raise Exception('手机号码输入错误')

            email = req.get('email')
            if email != None:
                if len(email) > 0 and re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)$', email) != None:
                    user.email = email
                else:
                    raise Exception('邮箱输入错误')

            password = req.get('password')
            if password != None:
                if len(password) > 0 and re.match(r"^(?![A-Za-z0-9]+$)(?![a-z0-9\\W]+$)(?![A-Za-z\\W]+$)(?![A-Z0-9\\W]+$)^.{8,}$", password) != None:
                    user.password = password
                else:
                    raise Exception('密码至少8位含大小写字母、数字、特殊符号的字符')

            avator = req.get('avator')
            if avator != None:
                if len(avator) != 0 and re.match(r'^http(s)?:\/\/([\w.]+\/?)\S*', avator) != None:
                    user.avator = avator
                else:
                    raise Exception('头像地址错误')
            
            user.save()
            return JsonResponse({ 'code': 0, 'data': [], 'message': '操作成功' })
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], 'message': str(e) })

    def getUserOne(id):
        try:
            res = models.Users.objects.get(id=id)
            return res.toJson()
        except:
            return []

    def getUsersList(page, size):

        res = models.Users.objects.all()[(page - 1) * size : page * size]
        json = []
        for i in res:
            json.append(i.toJson())

        total = models.Users.objects.count()
        return {
            'page': page,
            'size': size,
            'total': total,
            'list': json
        }

    
    @require_http_methods(['GET'])
    def getUsers(request):
        req = json.loads(request.body.decode('utf-8'))
        id = req.get('id')
        if id != None and isinstance(id, int) and id > 0:
            res = Users.getUserOne(id=id)
        else:
            page = req.get('page')
            size = req.get('size')
            res = Users.getUsersList(page=page, size=size)

        return JsonResponse({ 'code': 0, 'data': res, 'message': '操作成功' })
    
    @require_http_methods(['POST'])
    def login(request):
        try:
            req = json.loads(request.body.decode('utf-8'))
            username = req.get('username')
            if str(username) in ['', None]:
                raise Exception('账号不存在')
            
            password = req.get('password')
            if str(password) in ['', None]:
                raise Exception('密码不存在')

            res = models.Users.objects.get(
                Q(username=username) | Q(email=username) | Q(phone=username)
            )
            if res.password == password:
                user = res.toJson()
                return JsonResponse({ 'code': 0, 'data': user, 'message': '操作成功' })
            else:
                raise Exception('密码错误')
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], 'message': str(e) })