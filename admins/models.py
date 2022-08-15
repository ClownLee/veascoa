from django.db import models
import json

class Admins(models.Model):
    id = models.AutoField(primary_key=True)
    is_del = models.SmallIntegerField(default=0)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    avator = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 'admins'
        managed = False
    
    def toJson(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])