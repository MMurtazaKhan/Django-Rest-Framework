from statistics import mode
from django.db import models

# Create your models here.

class Student_Three(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField()
    city = models.CharField(max_length=200)