from django.utils.deprecation import MiddlewareMixin

class Interceptor(MiddlewareMixin):
    def process_request(self, request):
        print('在请求到达路由之前调用我')
        
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('调用视图之前先调用我')
        
    def process_response(self, request, response):
        print('当前响应返给浏览器之前先调用我，必须返回response')
        return response