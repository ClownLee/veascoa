from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    avator = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 'users'
        managed = False