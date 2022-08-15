from django.urls import path
from . import views

urlpatterns = [
    path('add-admin', views.Admins.addAdmin),
    path('update-admin', views.Admins.updateAdmin),
    path('get-admin', views.Admins.getAdmins),
]