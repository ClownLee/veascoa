from django.urls import path
from . import views

urlpatterns = [
    path('add', views.BaseInfo.addBaseInfo),
    path('update', views.BaseInfo.updateBaseInfo),
    path('get', views.BaseInfo.getBaseInfo),
]