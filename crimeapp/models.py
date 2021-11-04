from django.db import models

# Create your models here.

class year(models.Model):
     
    SNo = models.IntegerField() 
    crime = models.CharField(max_length=100)
    year2016 = models.IntegerField()
    year2017 = models.IntegerField()
    year2018 = models.IntegerField()
    