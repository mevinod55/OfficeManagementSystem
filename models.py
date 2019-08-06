from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=20)
    taskname = models.CharField(max_length=30)
    Assigndate = models.DateField()
    dateline = models.DateField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.name



