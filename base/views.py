# from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
class Base(View):

    @require_http_methods(['GET'])
    def index(request):
        # print(request.GET.get('id', default=None))
        return JsonResponse({ "name": "张三", "id": request.GET.get('id', default=None) })