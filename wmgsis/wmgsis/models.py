from django.db import models

# Each attribute of the nodel represents a database field

class Graduate(models.Model):
    graduate_name = models.CharField(max_length=20)
    cohort = models.CharField(max_length=20)
    salary = models.IntegerField()
    city = models.CharField(max_length=20)
    activity = models.CharField(max_length=20)
    degree_classifcation = models.CharField(max_length=20)
