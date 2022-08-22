import re, json
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from . import models
from utils.constants.index import IS_MASTER, IS_DEL
from utils.constants.education import EDUCATION

# Create your views here.
class Education(View):
    @require_http_methods(['POST'])
    def add(request):
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
            
            school = req.get('school')
            if str(school) in [None, '']:
                raise Exception('请填写学校名称')
            
            edu = req.get('edu')
            if str(edu) not in EDUCATION.keys():
                raise Exception('请选择学历')
            
            major = req.get('major')
            if str(major) in [None, '']:
                raise Exception('请填写专业名称')
            
            honor = req.get('honor')
            if str(honor) in [None, '']:
                raise Exception('请填写专业名称')
            
            start_time = req.get('start_time')
            if re.match(r'^[1-2][0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', str(start_time)) == None:
                raise Exception('请选择开始时间')

            end_time = req.get('end_time')
            if re.match(r'^[1-2][0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', str(end_time)) == None:
                raise Exception('请选择结束时间')

            education = models.Education(
                uid=uid,
                is_master=is_master,
                school=school,
                edu=edu,
                major=major,
                honor=honor,
                start_time=start_time,
                end_time=end_time,
            )
            education.save()

            return JsonResponse({ 'code': 0, 'data': [], 'message': '操作成功' })
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], 'message': str(e) })
    

    @require_http_methods(['POST'])
    def update(request):
        try:
            req = json.loads(request.body.decode('utf-8'))
            id = req.get('id')
            uid = req.get('uid')
            if not (id != None and isinstance(id, int) and id > 0):
                raise Exception('id不存在')
            
            if not (uid != None and isinstance(uid, int) and uid > 0):
                raise Exception('用户id不存在')

            education = models.Education.objects.get(id=id, uid=uid)

            is_master = req.get('is_master')
            if is_master != None:
                if int(is_master) not in IS_MASTER.keys():
                    raise Exception('请设置正确的是否主数据值')
                else:
                    education.is_master = is_master

            is_del = req.get('is_del')
            if is_del != None:
                if int(is_del) not in IS_DEL.keys():
                    raise Exception('是否删除的参数错误')
                else:
                    education.is_del = is_del

            school = req.get('school')
            if school not in  ['', None]:
                education.school = school
                
            edu = req.get('edu')
            if edu not in  ['', None] and edu in EDUCATION.keys():
                education.edu = edu

            major = req.get('major')
            if major not in  ['', None]:
                education.major = major
            
            honor = req.get('honor')
            if honor not in  ['', None]:
                education.honor = honor
            
            start_time = req.get('start_time')
            if start_time not in  ['', None] and re.match(r'^[1-2][0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', str(start_time)) != None:
                education.start_time = start_time

            end_time = req.get('end_time')
            if end_time not in  ['', None] and re.match(r'^[1-2][0-9]{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', str(end_time)) != None:
                education.end_time = end_time

            education.save()

            return JsonResponse({ 'code': 0, 'data': [], 'message': '操作成功' })
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], 'message': str(e) })

    @require_http_methods(['GET'])
    def getByUid(request):
        try:
            req = json.loads(request.body.decode('utf-8'))

            uid = req.get('uid')
            id = req.get('id')
            if uid == None or int(uid) <= 0:
                page = req.get('page')
                if page == None or int(page) < 1:
                    page = 1
                
                size = req.get('size')
                if size == None or int(size) <= 0:
                    size = 20
                
                res = models.Education.filter(uid=uid, is_del=0).all()[(page - 1) * size : page * size]

                lists = []
                for i in res:
                    lists.append(i.toJson())

                total = models.BaseInfo.objects.count()
                response = {
                    'page': page,
                    'size': size,
                    'total': total,
                    'list': lists
                }

            elif id == None or int(id) <= 0:
                res = models.Education.filter(is_del=0).get(id=id)
                response = res.toJson()
            else:
                page = req.get('page')
                if page == None or int(page) < 1:
                    page = 1
                
                size = req.get('size')
                if size == None or int(size) <= 0:
                    size = 20
                
                res = models.Education.filter(is_del=0).all()[(page - 1) * size : page * size]

                lists = []
                for i in res:
                    lists.append(i.toJson())

                total = models.BaseInfo.objects.count()
                response = {
                    'page': page,
                    'size': size,
                    'total': total,
                    'list': lists
                }

            return JsonResponse({ 'code': 0, 'data': response, 'message': '请求成功' })
        except Exception as e:
            return JsonResponse({ 'code': 1, 'data': [], 'message': str(e) })
