import json
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from utils.constants.index import IS_DEL, IS_MASTER
from utils.constants.education import EDUCATION
from utils.constants.nation import NATION
from utils.constants.sex import SEX
from utils.constants.politic import POLITIC

class Maps(View):

    @require_http_methods(['GET'])
    def getMaps(request):
        data = {
            'IS_DEL': IS_DEL,
            'IS_MASTER': IS_MASTER,
            'EDUCATION': EDUCATION,
            'NATION': NATION,
            'SEX': SEX,
            'POLITIC': POLITIC,
        }

        try:
            req = json.loads(request.body.decode('utf-8'))
            map = req.get('map')
            return JsonResponse({ 'code': 0, 'data': data[str(map).upper()], 'message': '请求成功' })
        except:
            return JsonResponse({ 'code': 0, 'data': data, 'message': '请求成功' })