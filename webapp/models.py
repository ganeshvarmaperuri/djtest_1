from django.db import models

# Create your models here.
class EmpModelForm(models.Model):
    EmpId = models.IntegerField()
    EmpName = models.CharField(max_length=50)
    EmpSal = models.IntegerField()
    EmpLoc = models.CharField(max_length=50)