from django.db import models
import json

class BaseInfo(models.Model):
    id = models.AutoField(primary_key=True)
    is_del = models.SmallIntegerField(default=0)
    is_master = models.SmallIntegerField(default=0)
    avator = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    political_outlook = models.CharField(max_length=255)
    nation = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    graduated_from = models.CharField(max_length=255)
    graduated_time = models.DateTimeField()
    education = models.CharField(max_length=255)
    self_evaluation = models.TextField()
    class Meta:
        db_table = 'base_info'
        managed = False
    
    def toJson(self):
        return dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]])