from django.urls import path
from . import views

urlpatterns = [
    path('add-admin', views.BaseInfo.addBaseInfo),
    path('update-admin', views.BaseInfo.updateBaseInfo),
    path('get-admin', views.BaseInfo.getBaseInfo),
]