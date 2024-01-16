from django.db import models

# Create your models here.


class User(models.Model):
    Emp_id = models.IntegerField(unique=True, blank=False, null=False)
    Name = models.CharField(max_length=120)
    Position = models.CharField(max_length=120)
    Department = models.CharField(max_length=120)
    Pay = models.FloatField()
    Grade = models.FloatField()
    Password = models.CharField(max_length=120, default='root')
