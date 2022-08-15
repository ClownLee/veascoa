from django.urls import path
from . import views

urlpatterns = [
    path('add-user', views.Users.addUser),
    path('update-user', views.Users.updateUser),
    path('get-users', views.Users.getUsers),
]