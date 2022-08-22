from django.urls import path
from . import views

urlpatterns = [
    path('add', views.Education.add),
    path('update', views.Education.update),
    path('get', views.Education.getByUid),
]