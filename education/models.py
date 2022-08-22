from django.db import models
from utils.tools.index import Tools

class Education(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.BigIntegerField()
    is_del = models.SmallIntegerField(default=0)
    is_master = models.SmallIntegerField(default=0)
    school = models.CharField(max_length=255)
    edu = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    honor = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'education'
        managed = False
        ordering = ('-create_time',)

    def toJson(self):
        return Tools.toJson(self)
