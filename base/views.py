# from django.shortcuts import render
import re
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from . import models

# Create your views here.
class Base(View):

    @require_http_methods(['GET'])
    def index(request):
        # print(request.GET.get('id', default=None))
        try:
            username = request.GET.get('username', default="")
            if len(username) < 6:
                raise Exception('用户名必须大于6个字符')

            phone = request.GET.get('phone', default="")
            if re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', phone) == None:
                raise Exception('手机号码输入错误')

            email = request.GET.get('email', default="")
            if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)$', email) == None:
                raise Exception('邮箱输入错误')

            password = request.GET.get('password', default="")
            if re.match(r"^(?![A-Za-z0-9]+$)(?![a-z0-9\\W]+$)(?![A-Za-z\\W]+$)(?![A-Z0-9\\W]+$)^.{8,}$", password) == None:
                raise Exception('密码至少8位含大小写字母、数字、特殊符号的字符')

            avator = request.GET.get('avator', default="")

            users = models.Users(username=username, phone=phone, email=email, password=password, avator=avator)
            users.save()
            return JsonResponse({ "code": 0, "data": [], "message": "操作成功" })
        except Exception as e:
            return JsonResponse({ "code": 1, "data": [], "message": str(e) })
    
    @require_http_methods(['GET'])
    def update(request):
        try:
            id = request.GET.get('id', default=None)
            if id == None or len(id) < 0:
                raise Exception('id不存在')
            
            username = request.GET.get('username', default="")
            if len(username) < 6:
                raise Exception('用户名必须大于6个字符')
        
            user = models.Users.objects.get(id=id)
            user.username = ''
            user.save()
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], 'message': str(e) })
