# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Base(View):
    def index(self):
        
        return HttpResponse("Hello async world!")