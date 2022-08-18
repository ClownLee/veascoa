# from django.shortcuts import render
import re, json
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from . import models
from utils.constants.index import IS_MASTER, IS_DEL
from utils.constants.sex import SEX
from utils.constants.politic import POLITIC
from utils.constants.nation import NATION
from utils.constants.education import EDUCATION

# Create your views here.
class BaseInfo(View):

    @require_http_methods(['POST'])
    def addBaseInfo(request):
        try:
            req = json.loads(request.body.decode('utf-8'))

            uid = req.get('uid')
            if uid == None or int(uid) <= 0:
                raise Exception('请指定用户ID')
            
            is_master = req.get('is_master')
            if is_master != None and int(is_master) not in IS_MASTER.keys():
                raise Exception('请设置正确的是否主数据值')
            else:
                is_master = 0

            avator = req.get('avator')
            if avator != None and re.match(r'^http(s)?:\/\/([\w.]+\/?)\S*', avator) == None:
                raise Exception('寸照地址错误')

            username = req.get('username')
            if re.match(r'^[a-zA-Z\u4E00-\u9FA5\uf900-\ufa2d\S]+$', str(username)) == None:
                raise Exception('用户名中文或英文')
    
            sex = req.get('sex')
            if sex not in SEX.keys():
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
            if str(political_outlook) not in POLITIC.keys():
                raise Exception('政治面貌输入错误')

            nation = req.get('nation')
            if str(nation) not in NATION.keys():
                raise Exception('民族输入错误')

            address = req.get('address')
            if str(address) == None or len(address) <= 0:
                raise Exception('常住地址错误')
            
            graduated_from = req.get('graduated_from')
            if str(graduated_from) == None or len(graduated_from) <= 0:
                raise Exception('请输入毕业院校')
            
            major = req.get('major')
            if str(major) == None or len(major) <= 0:
                raise Exception('请输入专业')
            
            self_evaluation = req.get('self_evaluation')
            if str(self_evaluation) == None or len(self_evaluation) <= 0:
                raise Exception('请输入自我评价')
            
            graduated_time = req.get('graduated_time')
            if re.match(r'^[1-2][0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', str(graduated_time)) == None:
                raise Exception('请毕业时间')

            education = req.get('education')
            if str(education) not in EDUCATION.keys():
                raise Exception('请选择学历')

            baseinfo = models.BaseInfo(
                uid=uid,
                is_master=is_master,
                avator=avator,
                username=username,
                sex=sex,
                birthday=birthday,
                email=email,
                phone=phone,
                political_outlook=political_outlook,
                nation=nation,
                address=address,
                graduated_from=graduated_from,
                major=major,
                self_evaluation=self_evaluation,
                graduated_time=graduated_time,
                education=education,
            )
            baseinfo.save()

            return JsonResponse({ 'code': 0, 'data': [], 'message': '操作成功' })
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], 'message': str(e) })

    @require_http_methods(['POST'])
    def updateBaseInfo(request):
        try:
            req = json.loads(request.body.decode('utf-8'))
            id = req.get('id')
            uid = req.get('uid')
            if not (id != None and isinstance(id, int) and id > 0):
                raise Exception('id不存在')
            
            if not (uid != None and isinstance(uid, int) and uid > 0):
                raise Exception('用户id不存在')

            baseinfo = models.BaseInfo.objects.get(id=id, uid=uid)

            is_master = req.get('is_master')
            if is_master != None and int(is_master) not in IS_MASTER.keys():
                raise Exception('请设置正确的是否主数据值')
            else:
                baseinfo.is_master = 0 if is_master != None else is_master

            avator = req.get('avator')
            if avator != None:
                if re.match(r'^http(s)?:\/\/([\w.]+\/?)\S*', avator) == None:
                    raise Exception('寸照地址错误')
                else:
                    baseinfo.avator = avator

            username = req.get('username')
            if username != None:
                if re.match(r'^[a-zA-Z\u4E00-\u9FA5\uf900-\ufa2d\S]+$', str(username)) == None:
                    raise Exception('用户名中文或英文')
                else:
                    baseinfo.username = username
    
            sex = req.get('sex')
            if sex != None:
                if sex not in SEX.keys():
                    raise Exception('请选择性别')
                else:
                    baseinfo.sex = sex
            
            birthday = req.get('birthday')
            if birthday != None:
                if re.match(r'^[1-2][0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', str(birthday)) == None:
                    raise Exception('请选择出生日期')
                else:
                    baseinfo.birthday = birthday

            email = req.get('email')
            if email != None:
                if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)$', str(email)) == None:
                    raise Exception('邮箱输入错误')
                else:
                    baseinfo.email = email
            
            phone = req.get('phone')
            if phone != None:
                if re.match(r'^1(3\d|4[5-9]|5[0-35-9]|6[567]|7[0-8]|8\d|9[0-35-9])\d{8}$', str(phone)) == None:
                    raise Exception('手机号码输入错误')
                else:
                    baseinfo.phone = phone

            political_outlook = req.get('political_outlook')
            if political_outlook != None:
                if str(political_outlook) not in POLITIC.keys():
                    raise Exception('政治面貌输入错误')
                else:
                    baseinfo.political_outlook = political_outlook

            nation = req.get('nation')
            if nation != None:
                if str(nation) not in NATION.keys():
                    raise Exception('民族输入错误')
                else:
                    baseinfo.nation = nation

            address = req.get('address')
            if address != None:
                if str(address) == None or len(address) <= 0:
                    raise Exception('常住地址错误')
                else:
                    baseinfo.address = address
            
            graduated_from = req.get('graduated_from')
            if graduated_from != None:
                if str(graduated_from) == None or len(graduated_from) <= 0:
                    raise Exception('请输入毕业院校')
                else:
                    baseinfo.graduated_from = graduated_from
            
            major = req.get('major')
            if major != None:
                if str(major) == None or len(major) <= 0:
                    raise Exception('请输入专业')
                else:
                    baseinfo.major = major
            
            self_evaluation = req.get('self_evaluation')
            if self_evaluation != None:
                if str(self_evaluation) == None or len(self_evaluation) <= 0:
                    raise Exception('请输入自我评价')
                else:
                    baseinfo.self_evaluation = self_evaluation
            
            graduated_time = req.get('graduated_time')
            if graduated_time != None:
                if re.match(r'^[1-2][0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', str(graduated_time)) == None:
                    raise Exception('请毕业时间')
                else:
                    baseinfo.graduated_time = graduated_time

            education = req.get('education')
            if education != None:
                if str(education) not in EDUCATION.keys():
                    raise Exception('请选择学历')
                else:
                    baseinfo.education = education
            
            baseinfo.save()

            return JsonResponse({ 'code': 0, 'data': [], 'message': '操作成功' })
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], 'message': str(e) })
        

    def getBaseInfoOne(id):
        try:
            res = models.BaseInfo.objects.get(id=id)
            return res.toJson()
        except:
            return []

    def getBaseInfoList(page, size, uid=None):
        if uid != None:
            res = models.BaseInfo.objects.filter(uid=uid).all()[(page - 1) * size : page * size]
        else:
            res = models.BaseInfo.objects.all()[(page - 1) * size : page * size]
        
        json = []
        for i in res:
            json.append(i.toJson())

        total = models.BaseInfo.objects.count()
        return {
            'page': page,
            'size': size,
            'total': total,
            'list': json
        }

    
    @require_http_methods(['GET'])
    def getBaseInfo(request):
        req = json.loads(request.body.decode('utf-8'))
        id = req.get('id')
        uid = req.get('uid')
        if id != None and isinstance(id, int) and id > 0:
            res = BaseInfo.getBaseInfoOne(id=id)
        
        elif uid != None and isinstance(uid, int) and uid > 0:
            page = req.get('page')
            size = req.get('size')
            res = BaseInfo.getBaseInfoList(page=page, size=size, uid=uid)
        else:
            page = req.get('page')
            size = req.get('size')
            res = BaseInfo.getBaseInfoList(page=page, size=size)

        return JsonResponse({ 'code': 0, 'data': res, 'message': '操作成功' })
