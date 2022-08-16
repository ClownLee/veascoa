from django.urls import path
from . import views

urlpatterns = [
    path('add', views.Admins.addAdmin),
    path('update', views.Admins.updateAdmin),
    path('get', views.Admins.getAdmins),
]