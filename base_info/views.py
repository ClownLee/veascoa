# from django.shortcuts import render
import re, json
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from . import models

# Create your views here.
class BaseInfo(View):

    @require_http_methods(['POST'])
    def addBaseInfo(request):
        try:
            req = json.loads(request.body.decode('utf-8'))

            is_master = req.get('is_master')
            if is_master != None and int(is_master) not in [0, 1]:
                raise Exception('请设置正确的是否主数据值')

            avator = req.get('avator')
            if avator != None and re.match(r'^http(s)?:\/\/([\w.]+\/?)\S*', avator) == None:
                raise Exception('寸照地址错误')

            username = req.get('username')
            if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]{5,11}$', str(username)) == None:
                raise Exception('用户名6-12个字符且必须以字母或下划线开头')
    
            sex = req.get('sex')
            if sex not in ['男', '女']:
                raise Exception('请选择性别')
            
            birthday = req.get('birthday')
            if re.match(r'^[1-2][0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', str(birthday)) == None:
                raise Exception('请选择出生日期')

            email = req.get('email')
            if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)$', str(email)) == None:
                raise Exception('邮箱输入错误')
            
            phone = req.get('phone')
            if re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', str(phone)) == None:
                raise Exception('手机号码输入错误')

            political_outlook = req.get('political_outlook')
            if political_outlook == None:
                raise Exception('手机号码输入错误')

            nation = req.get('nation')
            if re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', str(nation)) == None:
                raise Exception('手机号码输入错误')

            return JsonResponse({ "code": 0, "data": [], "message": "操作成功" })
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], message: str(e) })

    @require_http_methods(['POST'])
    def updateBaseInfo(request):
        pass

    @require_http_methods(['POST'])
    def getBaseInfo(request):
        pass
