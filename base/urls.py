from django.urls import path
from . import views

urlpatterns = [
    path('add-user', views.Base.addUser),
    path('update-user', views.Base.updateUser),
    path('get-users', views.Base.getUsers),
]