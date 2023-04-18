from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.


class Department(models.Model):
    departmentname = models.CharField(max_length=100)


    def __str__(self):
        return self.departmentname


class Course(models.Model):
    deptid = models.ForeignKey(Department,on_delete=CASCADE)

    coursename = models.CharField(max_length=100)
    fees = models.IntegerField()

    def __str__(self):
        return self.coursename
