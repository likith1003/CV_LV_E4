from django.db import models

# Create your models here.


class School(models.Model):
    sname = models.CharField(max_length=50)
    princy = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    add = models.CharField(max_length=50)

    def __str__(self):
        return self.sname
    

class Student(models.Model):
    sname = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schools')
    stdname = models.CharField(max_length=50)
    stdage = models.IntegerField()
    stdpno = models.CharField(max_length=50)
    stdadd = models.CharField(max_length=50)

    def __str__(self):
        return self.stdname