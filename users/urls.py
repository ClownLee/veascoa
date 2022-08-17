from django.urls import path
from . import views

urlpatterns = [
    path('add', views.Users.addUser),
    path('update', views.Users.updateUser),
    path('get', views.Users.getUsers),
    path('login', views.Users.login),
]