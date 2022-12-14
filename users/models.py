from django.db import models
from utils.tools.index import Tools

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    is_del = models.SmallIntegerField(default=0)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    avator = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'users'
        managed = False
        ordering = ('-create_time',)
    
    def toJson(self):
        return Tools.toJson(self)